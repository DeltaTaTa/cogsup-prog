"""Minimal drawing helper used by the exercises.

This provides two functions expected by the exercises:
- load(circles): store a reference to the currently active circles (no heavy logic)
- present_for(exp, circles, num_frames): attempt to plot stimuli if possible,
  otherwise fall back to waiting for the requested number of frames.

The implementation is intentionally tolerant so it won't crash the exercise when
run in environments where expyriment's full display stack isn't available.
"""
from __future__ import annotations

import time
from typing import List

_CURRENT_CIRCLES: List[object] = []


def load(circles: List[object]) -> None:
    """Store the list of circle stimuli for later presentation.

    This function intentionally does not try to draw anything. It only keeps a
    reference to the passed-in list so callers can reuse the same object.
    """
    global _CURRENT_CIRCLES
    # keep the same list object shape — copy contents
    _CURRENT_CIRCLES = list(circles)


def present_for(exp, circles: List[object], num_frames: int = 1, frame_rate: int = 60) -> None:
    """Present the supplied stimuli for num_frames frames.

    Behaviour:
    - If the stimulus objects expose a .plot(screen) or .plot() method we try
      to call it (errors are caught and ignored).
    - For each frame we attempt to use expyriment's timing (`control.wait`) if
      available. Otherwise we fall back to time.sleep.

    The function tolerates missing display backends so it can be used for smoke
    testing and headless runs.
    """
    # prefer the passed-in list; fallback to last-loaded
    if circles is None:
        circles = _CURRENT_CIRCLES

    frame_duration_s = 1.0 / float(frame_rate) if frame_rate > 0 else 1.0 / 60.0

    # try to import expyriment.control.wait for nicer timing, but it's optional
    control_wait_ms = None
    try:
        from expyriment import control as _control

        def _wait(ms: int) -> None:
            try:
                _control.wait(ms)
            except Exception:
                time.sleep(ms / 1000.0)

        control_wait_ms = _wait
    except Exception:
        control_wait_ms = None

    for _ in range(max(0, int(num_frames))):
        # attempt to plot each stimulus; ignore any plotting errors
        for c in (circles or []):
            try:
                # try common signatures
                if hasattr(c, "plot"):
                    try:
                        # many expyriment stimuli accept an optional screen arg
                        c.plot(getattr(exp, "screen", None))
                    except TypeError:
                        # plot() with no args
                        c.plot()
                    except Exception:
                        # last resort: try plot with no args
                        try:
                            c.plot()
                        except Exception:
                            pass
            except Exception:
                # ignore any errors plotting stimuli
                pass

        # wait one frame (prefer expyriment control.wait if available)
        if control_wait_ms is not None:
            try:
                control_wait_ms(int(round(frame_duration_s * 1000)))
            except Exception:
                time.sleep(frame_duration_s)
        else:
            time.sleep(frame_duration_s)
