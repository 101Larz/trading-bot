/**
 * Trading Bot Dashboard — client-side logic
 * - Auto-refresh every 60 s via polling /api/* endpoints
 * - Countdown timer in sidebar
 * - Market open/close status indicator
 * - Helper functions used by page-specific inline scripts
 */

const REFRESH_INTERVAL = 60; // seconds

let countdown = REFRESH_INTERVAL;
let refreshTimer = null;

// ── Countdown ticker ─────────────────────────────────────────────
function startCountdown() {
  countdown = REFRESH_INTERVAL;
  clearInterval(refreshTimer);

  refreshTimer = setInterval(() => {
    countdown--;
    const el = document.getElementById("refresh-timer");
    if (el) el.textContent = countdown + "s";

    if (countdown <= 0) {
      doRefresh();
    }
  }, 1000);
}

// ── Trigger a data refresh ────────────────────────────────────────
function doRefresh() {
  countdown = REFRESH_INTERVAL;
  // Each page defines its own window.refreshData(); fall back to reload.
  if (typeof window.refreshData === "function") {
    window.refreshData();
  } else {
    location.reload();
  }
  startCountdown();
}

// Called by the manual "↻ Refresh" button
function refreshNow() {
  doRefresh();
}

// ── Market status indicator ───────────────────────────────────────
function updateMarketStatus(clock) {
  const dot   = document.getElementById("status-dot");
  const label = document.getElementById("status-label");
  if (!dot || !label || !clock) return;

  if (clock.error) {
    dot.className   = "status-dot";
    label.textContent = "API error";
    return;
  }

  const isOpen = clock.is_open;
  dot.className = "status-dot " + (isOpen ? "open" : "closed");
  label.textContent = isOpen ? "Market open" : "Market closed";

  // Show time to next open/close
  const nextKey  = isOpen ? "next_close" : "next_open";
  const nextTime = clock[nextKey];
  if (nextTime) {
    const diffMs = new Date(nextTime) - new Date();
    if (diffMs > 0) {
      const h = Math.floor(diffMs / 3600000);
      const m = Math.floor((diffMs % 3600000) / 60000);
      const suffix = isOpen
        ? `closes in ${h}h ${m}m`
        : `opens in ${h}h ${m}m`;
      label.textContent += ` · ${suffix}`;
    }
  }
}

// ── DOM helpers used by page scripts ─────────────────────────────
function setText(id, text) {
  const el = document.getElementById(id);
  if (el) el.textContent = text;
}

function setSignedMoney(id, val) {
  const el = document.getElementById(id);
  if (!el) return;
  const f    = parseFloat(val) || 0;
  const sign = f > 0 ? "+" : "";
  el.textContent = sign + "$" + Math.abs(f).toLocaleString("en-US", { minimumFractionDigits: 2 });
  el.className = el.className.replace(/\b(positive|negative|neutral)\b/g, "")
               + " " + (f > 0 ? "positive" : f < 0 ? "negative" : "neutral");
}

// ── Boot ──────────────────────────────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
  startCountdown();

  // Poll market clock every 5 minutes independently of data refresh
  setInterval(() => {
    fetch("/api/clock")
      .then(r => r.json())
      .then(updateMarketStatus)
      .catch(() => {});
  }, 5 * 60 * 1000);
});
