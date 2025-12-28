"""
Application module for the watchdog PoC.
Implements a simple periodic task that signals a watchdog.
"""

import time
import threading
import logging

logger = logging.getLogger(__name__)


class Application:
    """Simple application that runs a periodic task and pets a watchdog."""

    def __init__(self, watchdog, interval: float = 1.0):
        """
        Args:
            watchdog: Watchdog instance with a `pet()` method.
            interval: Time in seconds between iterations.
        """
        self.watchdog = watchdog
        self.interval = interval
        self._stop_event = threading.Event()
        self._thread = None
        self._iteration = 0

    def _run_loop(self):
        """Main application loop."""
        logger.info("Application started.")
        while not self._stop_event.is_set():
            # Perform a trivial task
            self._iteration += 1
            logger.info(f"Iteration {self._iteration}: Performing task...")

            # Pet the watchdog to signal we are alive
            try:
                self.watchdog.pet()
            except Exception as e:
                logger.error(f"Failed to pet watchdog: {e}")

            # Sleep for the interval (simulate work)
            time.sleep(self.interval)

        logger.info("Application stopped.")

    def start(self):
        """Start the application in a background thread."""
        if self._thread is not None and self._thread.is_alive():
            logger.warning("Application already running.")
            return
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()
        logger.info("Application thread started.")

    def stop(self):
        """Stop the application."""
        self._stop_event.set()
        if self._thread is not None:
            self._thread.join(timeout=5.0)
            if self._thread.is_alive():
                logger.warning("Application thread did not finish in time.")
            else:
                logger.info("Application thread stopped.")
        self._thread = None

    def is_alive(self):
        """Check if the application thread is alive."""
        return self._thread is not None and self._thread.is_alive()


if __name__ == "__main__":
    # Simple test harness
    import sys
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Dummy watchdog for testing
    class DummyWatchdog:
        def pet(self):
            print("Watchdog petted.")

    watchdog = DummyWatchdog()
    app = Application(watchdog, interval=0.5)
    app.start()
    try:
        time.sleep(3)
    finally:
        app.stop()