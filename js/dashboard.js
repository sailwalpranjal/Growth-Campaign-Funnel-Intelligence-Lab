/**
 * web/js/dashboard.js
 * -------------------
 * Khatabook Growth Intelligence Platform Controller
 * Ultra-Premium Designer-Grade Engine with Real-Time Microinteractions:
 * - Real-Time Hover HUDs for sub-millisecond cursor data updates
 * - Dynamic Canvas Gradients & Pill-topped bars (replacing flat chunky charts)
 * - Multi-Mode Mix Standardization Switcher (Cost vs Variance Shift vs Weights)
 * - Stepped 3-Factor Waterfall with Lever Inspector HUD
 * - Multi-Stage Funnel Progression & 92.6% Leakage Beacon
 * - Khatabook App Funnel & 12-Month LTV/CAC Payback Scrubber
 * - Interactive Coordinate Reticle on Audience Bubble Matrix
 * - 60fps Laser Cursor Crosshair on Gaussian Bell Curves
 * - Consumer Intent Flow (UCI Dataset)
 * - ICE Growth Roadmap & Retro Verification Terminal
 */

// Global State
let DASHBOARD_DATA = null;
let waterfallChartInst = null;
let appFunnelChartInst = null;
let ltvCacPaybackChartInst = null;
let audienceBubbleChartInst = null;
let mixAdjustmentChartInst = null;
let consumerCohortChartInst = null;
let consumerTrafficChartInst = null;
let currentFunnelCamp = 1178;
let currentMixMode = 'cost';

// Set Global Chart.js Designer Defaults
if (window.Chart) {
  Chart.defaults.color = '#94A3B8';
  Chart.defaults.borderColor = 'rgba(255, 255, 255, 0.06)';
  Chart.defaults.font.family = "'Plus Jakarta Sans', sans-serif";
  Chart.defaults.plugins.tooltip.backgroundColor = 'rgba(8, 10, 16, 0.95)';
  Chart.defaults.plugins.tooltip.titleColor = '#F8FAFC';
  Chart.defaults.plugins.tooltip.bodyColor = '#CBD5E1';
  Chart.defaults.plugins.tooltip.borderColor = 'rgba(99, 102, 241, 0.35)';
  Chart.defaults.plugins.tooltip.borderWidth = 1;
  Chart.defaults.plugins.tooltip.padding = 12;
  Chart.defaults.plugins.tooltip.cornerRadius = 10;
  Chart.defaults.plugins.tooltip.displayColors = true;
  Chart.defaults.plugins.tooltip.boxPadding = 4;

  // Fluid physics-based cubic-bezier easing & progressive animations
  Chart.defaults.animation = {
    duration: 1000,
    easing: 'easeOutQuart',
  };
  Chart.defaults.transitions = {
    active: {
      animation: {
        duration: 250,
        easing: 'easeOutQuart'
      }
    }
  };
  // Ensure touch events are enabled for mobile microinteractions
  Chart.defaults.events = ['mousemove', 'mouseout', 'click', 'touchstart', 'touchmove', 'touchend'];
}

// Helper: Create vertical linear gradient on canvas
function createVGradient(ctx, colorTop, colorBottom, height = 300) {
  if (!ctx) return colorTop;
  const g = ctx.createLinearGradient(0, 0, 0, height);
  g.addColorStop(0, colorTop);
  g.addColorStop(1, colorBottom);
  return g;
}

// -----------------------------------------------------------------------------
// 1. TAB NAVIGATION & INITIALIZATION
// -----------------------------------------------------------------------------
function switchTab(tabId) {
  document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
  document.querySelectorAll('.tab-pill').forEach(el => el.classList.remove('active'));

  const activeContent = document.getElementById(`tab-${tabId}`);
  const activeBtn = document.getElementById(`tab-btn-${tabId}`);
  if (activeContent) activeContent.classList.remove('hidden');
  if (activeBtn) activeBtn.classList.add('active');

  // Trigger chart resizes on tab switch
  setTimeout(() => {
    if (tabId === 'waterfall' && waterfallChartInst) waterfallChartInst.resize();
    if (tabId === 'standardization' && mixAdjustmentChartInst) mixAdjustmentChartInst.resize();
    if (tabId === 'simulator') {
      if (appFunnelChartInst) appFunnelChartInst.resize();
      if (ltvCacPaybackChartInst) ltvCacPaybackChartInst.resize();
    }
    if (tabId === 'audience' && audienceBubbleChartInst) audienceBubbleChartInst.resize();
    if (tabId === 'ab-lab') drawBellCurves();
    if (tabId === 'consumer') {
      if (consumerCohortChartInst) consumerCohortChartInst.resize();
      if (consumerTrafficChartInst) consumerTrafficChartInst.resize();
    }
  }, 40);

  // Lazy render on first visit
  if (tabId === 'growth-os' && DASHBOARD_DATA?.growth_os && !window._growthOsRendered) {
    renderGrowthOS();
    window._growthOsRendered = true;
  }
  if (tabId === 'market-intel' && DASHBOARD_DATA?.market_intelligence && !window._marketIntelRendered) {
    renderMarketIntel();
    window._marketIntelRendered = true;
  }
}

document.addEventListener('DOMContentLoaded', async () => {
  await initDashboard();
});

async function initDashboard() {
  try {
    const res = await fetch('data/dashboard_data.json');
    if (res.ok) {
      DASHBOARD_DATA = await res.json();
    } else {
      throw new Error('Network fetch failed');
    }
  } catch (err) {
    console.warn('[!] Using standalone embedded payload:', err);
    DASHBOARD_DATA = getFallbackData();
  }

  // Render all modules
  renderScorecard();
  renderWaterfallChart();
  setFunnelView(1178);
  renderMixAdjustmentChart();
  initAppSimulator();
  renderAudienceBubbleChart();
  calculateLiveAB();
  renderConsumerCharts();
  renderExperiments('all');
  renderQualityAuditTerminal();
  
  if (DASHBOARD_DATA && DASHBOARD_DATA.growth_os) {
    renderGrowthOS();
    window._growthOsRendered = true;
  }
  if (DASHBOARD_DATA && DASHBOARD_DATA.market_intelligence) {
    renderMarketIntel();
    window._marketIntelRendered = true;
  }

  // Attach Bell Curve Interactive Crosshair
  initBellCurveCrosshair();

  if (window.lucide) {
    lucide.createIcons();
  }
}

// -----------------------------------------------------------------------------
// 2. TAB 1: EXECUTIVE SCORECARD
// -----------------------------------------------------------------------------
function renderScorecard() {
  const tbody = document.getElementById('scorecard-tbody');
  if (!tbody || !DASHBOARD_DATA) return;
  tbody.innerHTML = '';

  DASHBOARD_DATA.scorecard.forEach(row => {
    const tr = document.createElement('tr');
    tr.className = 'hover:bg-white/[0.03] transition-colors';
    tr.innerHTML = `
      <td class="px-4 py-3 font-bold text-white flex items-center gap-2">
        <span class="w-2.5 h-2.5 rounded-full ${row.campaign_id === 1178 ? 'bg-brandRose shadow-lg shadow-rose-500/50' : 'bg-brandCyan shadow-lg shadow-cyan-500/50'}"></span>
        Campaign ${row.campaign_id}
      </td>
      <td class="px-4 py-3 text-slate-400">${row.total_ads}</td>
      <td class="px-4 py-3 text-slate-300">${Number(row.total_impressions).toLocaleString()}</td>
      <td class="px-4 py-3 text-slate-300">${Number(row.total_clicks).toLocaleString()}</td>
      <td class="px-4 py-3 text-white font-semibold">$${Number(row.total_spend).toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}</td>
      <td class="px-4 py-3 text-brandEmerald font-bold">${row.approved_conversions}</td>
      <td class="px-4 py-3 text-slate-300">${(row.ctr * 100).toFixed(4)}%</td>
      <td class="px-4 py-3 text-slate-300">$${row.cpm.toFixed(3)}</td>
      <td class="px-4 py-3 ${row.click_to_approved_conv_rate < 0.03 ? 'text-brandRose font-bold' : 'text-slate-200'}">${(row.click_to_approved_conv_rate * 100).toFixed(2)}%</td>
      <td class="px-4 py-3 text-right font-bold ${row.cost_per_approved_conv > 50 ? 'text-brandRose' : 'text-brandEmerald'}">$${row.cost_per_approved_conv.toFixed(2)}</td>
    `;
    tbody.appendChild(tr);
  });
}

// -----------------------------------------------------------------------------
// 3. TAB 2: 3-FACTOR WATERFALL DECOMPOSITION (WITH REAL-TIME HUD)
// -----------------------------------------------------------------------------
function renderWaterfallChart() {
  const canvas = document.getElementById('waterfallChart');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  const labels = [
    'Baseline (Camp 936)',
    '1. CPM Effect (Cheaper Buying)',
    '2. CTR Resonance Decay',
    '3. Post-Click Conv Collapse',
    'Scaled (Camp 1178)'
  ];

  // Floating Bars [start, end]
  const dataBars = [
    [0, 15.81],
    [15.81, 12.07],
    [12.07, 16.73],
    [16.73, 63.83],
    [0, 63.83]
  ];

  // Gradients for each bar
  const bgColors = [
    createVGradient(ctx, 'rgba(99, 102, 241, 0.95)', 'rgba(99, 102, 241, 0.25)', 350),
    createVGradient(ctx, 'rgba(16, 185, 129, 0.95)', 'rgba(16, 185, 129, 0.25)', 350),
    createVGradient(ctx, 'rgba(245, 158, 11, 0.95)', 'rgba(245, 158, 11, 0.25)', 350),
    createVGradient(ctx, 'rgba(244, 63, 94, 0.95)', 'rgba(244, 63, 94, 0.25)', 350),
    createVGradient(ctx, 'rgba(139, 92, 246, 0.95)', 'rgba(139, 92, 246, 0.25)', 350)
  ];

  const borderColors = ['#818CF8', '#34D399', '#FBBF24', '#FB7185', '#A78BFA'];

  if (waterfallChartInst) waterfallChartInst.destroy();

  waterfallChartInst = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Cost per Approved ($)',
        data: dataBars,
        backgroundColor: bgColors,
        borderColor: borderColors,
        borderWidth: 1.5,
        borderRadius: { topLeft: 8, topRight: 8, bottomLeft: 4, bottomRight: 4 },
        borderSkipped: false,
        maxBarThickness: 52
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      animation: {
        duration: 1100,
        easing: 'easeOutQuart',
        delay: (ctx) => (ctx.type === 'data' && ctx.mode === 'default') ? ctx.dataIndex * 130 : 0
      },
      onHover: (event, elements) => {
        const hudTitle = document.getElementById('wf-hud-title');
        const hudVal = document.getElementById('wf-hud-value');
        const hudShare = document.getElementById('wf-hud-share');
        const hudVerdict = document.getElementById('wf-hud-verdict');
        const hudDot = document.getElementById('wf-hud-dot');

        if (elements.length > 0) {
          const idx = elements[0].index;
          if (idx === 0) {
            hudTitle.innerText = 'BASELINE: CAMPAIGN 936';
            hudVal.innerText = 'Unit Cost: $15.81 per Approved Lead (Mid-Scale Reference)';
            hudShare.innerText = 'Baseline Level';
            hudVerdict.innerText = 'Healthy Acquisition Benchmark';
            hudDot.className = 'w-3 h-3 rounded-full bg-brandIndigo animate-ping';
          } else if (idx === 1) {
            hudTitle.innerText = 'LEVER 1: CPM EFFECT (-$3.74)';
            hudVal.innerText = 'Formula: (CPM_1/1000 - CPM_0/1000) / (CTR_0 * CR_0) = -$3.74';
            hudShare.innerText = '-7.8% Offset';
            hudVerdict.innerText = 'Cheaper Media Inventory at Scale (-23.6% CPM)';
            hudDot.className = 'w-3 h-3 rounded-full bg-brandEmerald animate-ping';
          } else if (idx === 2) {
            hudTitle.innerText = 'LEVER 2: CTR RESONANCE DECAY (+$4.66)';
            hudVal.innerText = 'Formula: CPM_1/1000 * (1/CTR_1 - 1/CTR_0) / CR_0 = +$4.66';
            hudShare.innerText = '+9.7% Inflation';
            hudVerdict.innerText = 'Creative Fatigue from Broad Audience Reach (-27.9% CTR)';
            hudDot.className = 'w-3 h-3 rounded-full bg-brandAmber animate-ping';
          } else if (idx === 3) {
            hudTitle.innerText = 'LEVER 3: POST-CLICK CONVERSION COLLAPSE (+$47.10)';
            hudVal.innerText = 'Formula: (CPM_1/1000) / CTR_1 * (1/CR_1 - 1/CR_0) = +$47.10';
            hudShare.innerText = '98.1% of Cost Surge';
            hudVerdict.innerText = 'PRIMARY BOTTLENECK: 92.6% Form Drop-off Post-Click';
            hudDot.className = 'w-3 h-3 rounded-full bg-brandRose animate-ping';
          } else if (idx === 4) {
            hudTitle.innerText = 'FINAL SCALED: CAMPAIGN 1178 ($63.83)';
            hudVal.innerText = 'Unit Cost: $63.83 per Approved Lead (+303.7% vs Baseline)';
            hudShare.innerText = '+$48.02 Total Gap';
            hudVerdict.innerText = 'Exact Reconciled Identity (Residual: $0.00000000)';
            hudDot.className = 'w-3 h-3 rounded-full bg-brandViolet animate-ping';
          }
        }
      },
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: function(context) {
              const raw = context.raw;
              const delta = raw[1] - raw[0];
              if (context.dataIndex === 0) return `Baseline CPA: $${raw[1].toFixed(2)}`;
              if (context.dataIndex === 4) return `Scaled CPA: $${raw[1].toFixed(2)} (+303.7%)`;
              return `Variance Delta: ${delta >= 0 ? '+' : ''}$${delta.toFixed(2)} | Level: $${raw[1].toFixed(2)}`;
            }
          }
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          grid: { color: 'rgba(255, 255, 255, 0.05)' },
          ticks: { callback: v => '$' + v }
        },
        x: { grid: { display: false } }
      }
    }
  });
}

// -----------------------------------------------------------------------------
// 4. TAB 4: MIX STANDARDIZATION OVERHAUL (PER USER SCREENSHOT)
// -----------------------------------------------------------------------------
function setMixChartMode(mode) {
  currentMixMode = mode;
  ['cost', 'shift', 'weights'].forEach(m => {
    const btn = document.getElementById(`btn-mix-${m}`);
    if (btn) {
      if (m === mode) {
        btn.className = 'chart-view-btn active px-3 py-1.5 rounded-lg transition-all';
      } else {
        btn.className = 'chart-view-btn px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition-all';
      }
    }
  });
  renderMixAdjustmentChart();
}

function renderMixAdjustmentChart() {
  const canvas = document.getElementById('mixAdjustmentChart');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  if (mixAdjustmentChartInst) mixAdjustmentChartInst.destroy();

  // Gradients for Mode A: Cost Comparison
  const gradObserved = createVGradient(ctx, 'rgba(99, 102, 241, 0.95)', 'rgba(79, 70, 229, 0.3)', 280);
  const gradAdjusted = createVGradient(ctx, 'rgba(14, 165, 233, 0.95)', 'rgba(56, 189, 248, 0.3)', 280);

  let chartConfig = {};

  if (currentMixMode === 'cost') {
    chartConfig = {
      type: 'bar',
      data: {
        labels: ['Campaign 936 (Baseline)', 'Campaign 1178 (Scaled)'],
        datasets: [
          {
            label: 'Raw Observed Cost ($)',
            data: [15.81, 63.83],
            backgroundColor: gradObserved,
            borderColor: '#818CF8',
            borderWidth: 1.5,
            borderRadius: { topLeft: 8, topRight: 8 },
            maxBarThickness: 38
          },
          {
            label: 'Mix-Adjusted Standardized Cost ($)',
            data: [23.69, 78.16],
            backgroundColor: gradAdjusted,
            borderColor: '#38BDF8',
            borderWidth: 1.5,
            borderRadius: { topLeft: 8, topRight: 8 },
            maxBarThickness: 38
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        animation: {
          duration: 1100,
          easing: 'easeOutQuart',
          delay: (ctx) => (ctx.type === 'data' && ctx.mode === 'default') ? ctx.dataIndex * 130 + (ctx.datasetIndex || 0) * 110 : 0
        },
        onHover: (event, elements) => {
          const title = document.getElementById('mix-hud-title');
          const val = document.getElementById('mix-hud-val');
          const shift = document.getElementById('mix-hud-shift');
          const ratio = document.getElementById('mix-hud-ratio');
          const dot = document.getElementById('mix-hud-dot');

          if (elements.length > 0) {
            const dataIdx = elements[0].index;
            const dsIdx = elements[0].datasetIndex;

            if (dataIdx === 0) {
              title.innerText = 'CAMPAIGN 936 (BASELINE BENCHMARK)';
              val.innerText = dsIdx === 0 ? 'Raw Observed Cost: $15.81' : 'Mix-Adjusted Cost: $23.69 under Pooled Audience';
              shift.innerText = '+$7.88 (+49.8% Shift)';
              ratio.innerText = 'Demographic Re-weighting';
              dot.className = 'w-3 h-3 rounded-full bg-brandCyan animate-ping';
            } else {
              title.innerText = 'CAMPAIGN 1178 (SCALED CAMPAIGN)';
              val.innerText = dsIdx === 0 ? 'Raw Observed Cost: $63.83' : 'Mix-Adjusted Cost: $78.16 under Pooled Audience';
              shift.innerText = '+$14.33 (+22.5% Shift)';
              ratio.innerText = 'Cost Gap Persists at 3.3x';
              dot.className = 'w-3 h-3 rounded-full bg-brandRose animate-ping';
            }
          }
        },
        plugins: {
          legend: {
            position: 'top',
            labels: { boxWidth: 12, font: { size: 11 } }
          },
          tooltip: {
            callbacks: {
              label: ctx => `${ctx.dataset.label}: $${ctx.raw.toFixed(2)}`
            }
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            grid: { color: 'rgba(255, 255, 255, 0.05)' },
            ticks: { callback: v => '$' + v }
          },
          x: { grid: { display: false } }
        }
      }
    };
  } else if (currentMixMode === 'shift') {
    // Mode B: Standardization Shift Delta ($)
    const gradShift936 = createVGradient(ctx, 'rgba(56, 189, 248, 0.9)', 'rgba(14, 165, 233, 0.25)', 250);
    const gradShift1178 = createVGradient(ctx, 'rgba(244, 63, 94, 0.9)', 'rgba(225, 29, 72, 0.25)', 250);

    chartConfig = {
      type: 'bar',
      data: {
        labels: ['Campaign 936 Shift (+$7.88)', 'Campaign 1178 Shift (+$14.33)'],
        datasets: [{
          label: 'Standardization Cost Shift ($)',
          data: [7.88, 14.33],
          backgroundColor: [gradShift936, gradShift1178],
          borderColor: ['#38BDF8', '#FB7185'],
          borderWidth: 1.5,
          borderRadius: { topLeft: 8, topRight: 8 },
          maxBarThickness: 48
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        animation: {
          duration: 1000,
          easing: 'easeOutQuart',
          delay: (ctx) => (ctx.type === 'data' && ctx.mode === 'default') ? ctx.dataIndex * 150 : 0
        },
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: ctx => `Standardization Shift: +$${ctx.raw.toFixed(2)}`
            }
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            grid: { color: 'rgba(255, 255, 255, 0.05)' },
            ticks: { callback: v => '+$' + v }
          },
          x: { grid: { display: false } }
        }
      }
    };
  } else if (currentMixMode === 'weights') {
    // Mode C: Audience Mix Weights
    chartConfig = {
      type: 'bar',
      data: {
        labels: ['Age 30-34', 'Age 35-39', 'Age 40-44', 'Age 45-49'],
        datasets: [
          {
            label: 'Camp 936 Clicks (%)',
            data: [27.4, 28.6, 21.3, 22.7],
            backgroundColor: 'rgba(99, 102, 241, 0.8)',
            borderColor: '#818CF8',
            borderWidth: 1.5,
            borderRadius: 4
          },
          {
            label: 'Camp 1178 Clicks (%)',
            data: [35.2, 24.8, 18.9, 21.1],
            backgroundColor: 'rgba(244, 63, 94, 0.8)',
            borderColor: '#FB7185',
            borderWidth: 1.5,
            borderRadius: 4
          },
          {
            label: 'Pooled Benchmark Weight (%)',
            data: [34.8, 25.0, 19.0, 21.2],
            backgroundColor: 'rgba(16, 185, 129, 0.8)',
            borderColor: '#34D399',
            borderWidth: 1.5,
            borderRadius: 4
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        animation: {
          duration: 1000,
          easing: 'easeOutQuart',
          delay: (ctx) => (ctx.type === 'data' && ctx.mode === 'default') ? ctx.dataIndex * 90 + (ctx.datasetIndex || 0) * 80 : 0
        },
        plugins: {
          legend: { position: 'top', labels: { boxWidth: 12 } },
          tooltip: {
            callbacks: {
              label: ctx => `${ctx.dataset.label}: ${ctx.raw}%`
            }
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            grid: { color: 'rgba(255, 255, 255, 0.05)' },
            ticks: { callback: v => v + '%' }
          },
          x: { grid: { display: false } }
        }
      }
    };
  }

  mixAdjustmentChartInst = new Chart(ctx, chartConfig);
}

// -----------------------------------------------------------------------------
// 5. TAB 3: MULTI-STAGE STEP FUNNEL FLOW
// -----------------------------------------------------------------------------
function setFunnelView(campId) {
  currentFunnelCamp = campId;
  const btn1178 = document.getElementById('funnel-toggle-1178');
  const btn936 = document.getElementById('funnel-toggle-936');

  if (campId === 1178) {
    btn1178.className = 'px-3.5 py-1.5 rounded-lg bg-rose-500/20 text-brandRose border border-rose-500/30 font-bold transition-all';
    btn936.className = 'px-3.5 py-1.5 rounded-lg text-slate-400 hover:text-white transition-all';
  } else {
    btn936.className = 'px-3.5 py-1.5 rounded-lg bg-sky-500/20 text-brandCyan border border-sky-500/30 font-bold transition-all';
    btn1178.className = 'px-3.5 py-1.5 rounded-lg text-slate-400 hover:text-white transition-all';
  }

  renderFunnelSteps();
}

function renderFunnelSteps() {
  const container = document.getElementById('funnel-steps-container');
  if (!container) return;

  const data = currentFunnelCamp === 1178 ? {
    impressions: 204823716,
    clicks: 36068,
    enquiries: 2669,
    approved: 872,
    ctr: 0.0176,
    clickToEnquiry: 7.40,
    enquiryToApproved: 32.67,
    clickToApproved: 2.42,
    leakageDrop: 33484
  } : {
    impressions: 8143820,
    clicks: 1984,
    enquiries: 537,
    approved: 183,
    ctr: 0.0244,
    clickToEnquiry: 27.07,
    enquiryToApproved: 34.08,
    clickToApproved: 9.22,
    leakageDrop: 1447
  };

  container.innerHTML = `
    <!-- Step 1: Impressions -->
    <div class="p-4 rounded-xl bg-slate-950/60 border border-white/5 space-y-2 hover:border-white/15 transition-all">
      <div class="flex justify-between items-center text-xs font-mono">
        <span class="text-slate-400 font-bold flex items-center gap-2">
          <span class="w-5 h-5 rounded-full bg-slate-800 text-white flex items-center justify-center text-[10px]">1</span>
          Stage 1: Top-of-Funnel Impressions
        </span>
        <span class="text-white font-bold text-sm">${Number(data.impressions).toLocaleString()}</span>
      </div>
      <div class="w-full h-2.5 bg-slate-900 rounded-full overflow-hidden">
        <div class="h-full bg-gradient-to-r from-slate-600 to-slate-400 rounded-full" style="width: 100%"></div>
      </div>
      <div class="flex justify-between text-[11px] font-mono text-slate-500">
        <span>Paid Audience Reach</span>
        <span>100.0% Initial Traffic</span>
      </div>
    </div>

    <!-- Drop-off connector 1 -->
    <div class="flex items-center justify-center -my-2 text-[11px] font-mono text-slate-500">
      <span>&#8595; Creative Pass-Through: CTR = <strong class="text-brandCyan">${data.ctr.toFixed(4)}%</strong></span>
    </div>

    <!-- Step 2: Clicks -->
    <div class="p-4 rounded-xl bg-slate-950/60 border border-white/5 space-y-2 hover:border-sky-500/30 transition-all">
      <div class="flex justify-between items-center text-xs font-mono">
        <span class="text-slate-400 font-bold flex items-center gap-2">
          <span class="w-5 h-5 rounded-full bg-sky-950 text-brandCyan border border-sky-800 flex items-center justify-center text-[10px]">2</span>
          Stage 2: Ad Clicks (Landing Page Traffic)
        </span>
        <span class="text-brandCyan font-bold text-sm">${Number(data.clicks).toLocaleString()}</span>
      </div>
      <div class="w-full h-2.5 bg-slate-900 rounded-full overflow-hidden">
        <div class="h-full bg-gradient-to-r from-sky-600 to-brandCyan rounded-full" style="width: 100%"></div>
      </div>
      <div class="flex justify-between text-[11px] font-mono text-slate-500">
        <span>Cost per Click (CPC): $${(currentFunnelCamp === 1178 ? 1.54 : 1.46).toFixed(2)}</span>
        <span>100% of Landing Traffic</span>
      </div>
    </div>

    <!-- Drop-off connector 2 (THE BOTTLENECK) -->
    <div class="flex items-center justify-between p-3.5 rounded-xl ${currentFunnelCamp === 1178 ? 'bg-rose-950/40 border border-rose-800/60 text-rose-300 shadow-lg shadow-rose-950/40' : 'bg-slate-900 border border-white/10 text-slate-400'} text-xs font-mono">
      <span class="flex items-center gap-2 font-bold">
        ${currentFunnelCamp === 1178 ? '<span class="w-2.5 h-2.5 rounded-full bg-rose-500 animate-ping"></span> MASSIVE DROP-OFF BOTTLENECK:' : 'Stage 2 $\\to$ 3 Transition:'}
      </span>
      <span>Enquiry Form Completion: <strong class="${currentFunnelCamp === 1178 ? 'text-brandRose' : 'text-brandEmerald'} font-bold">${data.clickToEnquiry.toFixed(2)}%</strong> (${Number(data.leakageDrop).toLocaleString()} visitors bounced)</span>
    </div>

    <!-- Step 3: Total Conversions (Enquiries) -->
    <div class="p-4 rounded-xl bg-slate-950/60 border border-white/5 space-y-2 hover:border-amber-500/30 transition-all">
      <div class="flex justify-between items-center text-xs font-mono">
        <span class="text-slate-400 font-bold flex items-center gap-2">
          <span class="w-5 h-5 rounded-full bg-amber-950 text-brandAmber border border-amber-800 flex items-center justify-center text-[10px]">3</span>
          Stage 3: Submitted Enquiries / Leads
        </span>
        <span class="text-brandAmber font-bold text-sm">${Number(data.enquiries).toLocaleString()}</span>
      </div>
      <div class="w-full h-2.5 bg-slate-900 rounded-full overflow-hidden">
        <div class="h-full bg-gradient-to-r from-amber-600 to-brandAmber rounded-full" style="width: ${data.clickToEnquiry}%"></div>
      </div>
      <div class="flex justify-between text-[11px] font-mono text-slate-500">
        <span>Click-to-Enquiry Rate: ${data.clickToEnquiry.toFixed(2)}%</span>
        <span>${((data.enquiries / data.clicks) * 100).toFixed(1)}% of landing traffic retained</span>
      </div>
    </div>

    <!-- Drop-off connector 3 -->
    <div class="flex items-center justify-center -my-2 text-[11px] font-mono text-slate-500">
      <span>&#8595; Sales & Credit Approval: <strong class="text-brandEmerald font-bold">${data.enquiryToApproved.toFixed(2)}%</strong> (Near Parity across both campaigns)</span>
    </div>

    <!-- Step 4: Approved Conversions -->
    <div class="p-4 rounded-xl bg-slate-950/60 border border-white/5 space-y-2 hover:border-emerald-500/30 transition-all">
      <div class="flex justify-between items-center text-xs font-mono">
        <span class="text-slate-400 font-bold flex items-center gap-2">
          <span class="w-5 h-5 rounded-full bg-emerald-950 text-brandEmerald border border-emerald-800 flex items-center justify-center text-[10px]">4</span>
          Stage 4: Qualified & Approved Conversions
        </span>
        <span class="text-brandEmerald font-bold text-sm">${Number(data.approved).toLocaleString()}</span>
      </div>
      <div class="w-full h-2.5 bg-slate-900 rounded-full overflow-hidden">
        <div class="h-full bg-gradient-to-r from-emerald-600 to-brandEmerald rounded-full" style="width: ${data.clickToApproved * 4}%"></div>
      </div>
      <div class="flex justify-between text-[11px] font-mono text-slate-500">
        <span>Enquiry-to-Approved Rate: ${data.enquiryToApproved.toFixed(2)}%</span>
        <span class="text-brandEmerald font-bold">End-to-End Click $\\to$ Approved: ${data.clickToApproved.toFixed(2)}%</span>
      </div>
    </div>
  `;
}

// -----------------------------------------------------------------------------
// 6. TAB 5: KHATABOOK APP & LTV SIMULATOR (WITH TIMELINE SCRUBBER HUD)
// -----------------------------------------------------------------------------
function initAppSimulator() {
  updateAppSimulator();
}

function resetSimulatorDefaults() {
  document.getElementById('sim-budget').value = 500000;
  document.getElementById('sim-cpi').value = 35;
  document.getElementById('sim-otp').value = 82;
  document.getElementById('sim-d1').value = 42;
  document.getElementById('sim-d7').value = 28;
  document.getElementById('sim-soundbox').value = 15;
  updateAppSimulator();
}

function updateAppSimulator() {
  const budget = parseFloat(document.getElementById('sim-budget').value);
  const cpi = parseFloat(document.getElementById('sim-cpi').value);
  const otpRate = parseFloat(document.getElementById('sim-otp').value) / 100;
  const d1Rate = parseFloat(document.getElementById('sim-d1').value) / 100;
  const d7Rate = parseFloat(document.getElementById('sim-d7').value) / 100;
  const soundboxRate = parseFloat(document.getElementById('sim-soundbox').value) / 100;

  // Update slider displays
  document.getElementById('sim-budget-val').innerText = '₹' + Number(budget).toLocaleString();
  document.getElementById('sim-cpi-val').innerText = '₹' + cpi;
  document.getElementById('sim-otp-val').innerText = (otpRate * 100).toFixed(0) + '%';
  document.getElementById('sim-d1-val').innerText = (d1Rate * 100).toFixed(0) + '%';
  document.getElementById('sim-d7-val').innerText = (d7Rate * 100).toFixed(0) + '%';
  document.getElementById('sim-soundbox-val').innerText = (soundboxRate * 100).toFixed(0) + '%';

  // Funnel Volumes
  const totalInstalls = Math.round(budget / cpi);
  const otpVerified = Math.round(totalInstalls * otpRate);
  const d1Active = Math.round(otpVerified * d1Rate);
  const d7Retained = Math.round(d1Active * d7Rate);
  const soundboxMerchants = Math.round(d1Active * soundboxRate);

  // Unit Economics
  const merchantCAC = budget / Math.max(1, d1Active);
  const monthlySoundboxRev = 125 * soundboxRate;
  const monthlyUpiMargin = 22;
  const monthlyLendingMargin = 14;
  const monthlyMarginPerMerchant = monthlySoundboxRev + monthlyUpiMargin + monthlyLendingMargin;

  // 12-Month LTV Curve
  let cumulativeLTV = [];
  let runningTotalLTV = 0;

  for (let m = 1; m <= 12; m++) {
    const activeMultiplier = Math.max(0.20, Math.pow(d7Rate, m * 0.25));
    runningTotalLTV += monthlyMarginPerMerchant * activeMultiplier;
    cumulativeLTV.push(runningTotalLTV);
  }

  const netLTV12M = runningTotalLTV;
  const ltvCacRatio = netLTV12M / Math.max(1, merchantCAC);
  const paybackMonths = Math.min(12, merchantCAC / Math.max(1, monthlyMarginPerMerchant));

  document.getElementById('sim-out-installs').innerText = Number(totalInstalls).toLocaleString();
  document.getElementById('sim-out-active').innerText = Number(d1Active).toLocaleString();
  document.getElementById('sim-out-cac').innerText = '₹' + merchantCAC.toFixed(2);
  document.getElementById('sim-out-payback').innerText = paybackMonths < 12 ? paybackMonths.toFixed(1) + ' Months' : '> 12 Months';
  
  const ltvcacEl = document.getElementById('sim-out-ltvcac');
  ltvcacEl.innerText = ltvCacRatio.toFixed(1) + 'x';
  if (ltvCacRatio >= 3.0) {
    ltvcacEl.className = 'font-bold text-brandEmerald';
  } else if (ltvCacRatio >= 1.5) {
    ltvcacEl.className = 'font-bold text-brandAmber';
  } else {
    ltvcacEl.className = 'font-bold text-brandRose';
  }

  renderAppFunnelChart(totalInstalls, otpVerified, d1Active, d7Retained, soundboxMerchants);
  renderLtvCacPaybackChart(merchantCAC, cumulativeLTV);
}

function renderAppFunnelChart(installs, otp, d1, d7, soundbox) {
  const canvas = document.getElementById('appFunnelChart');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  if (appFunnelChartInst) appFunnelChartInst.destroy();

  const gInst = createVGradient(ctx, 'rgba(56, 189, 248, 0.9)', 'rgba(14, 165, 233, 0.25)', 250);
  const gOtp = createVGradient(ctx, 'rgba(99, 102, 241, 0.9)', 'rgba(79, 70, 229, 0.25)', 250);
  const gD1 = createVGradient(ctx, 'rgba(16, 185, 129, 0.95)', 'rgba(5, 150, 105, 0.25)', 250);
  const gD7 = createVGradient(ctx, 'rgba(245, 158, 11, 0.9)', 'rgba(217, 119, 6, 0.25)', 250);
  const gSb = createVGradient(ctx, 'rgba(139, 92, 246, 0.95)', 'rgba(124, 58, 237, 0.25)', 250);

  appFunnelChartInst = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Play Store Installs', 'OTP Verified', 'D1 Active Ledger', 'D7 Retained', 'Soundbox Merchants'],
      datasets: [{
        label: 'Merchants',
        data: [installs, otp, d1, d7, soundbox],
        backgroundColor: [gInst, gOtp, gD1, gD7, gSb],
        borderColor: ['#38BDF8', '#818CF8', '#34D399', '#FBBF24', '#A78BFA'],
        borderWidth: 1.5,
        borderRadius: { topLeft: 8, topRight: 8 },
        maxBarThickness: 42
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      animation: {
        duration: 1100,
        easing: 'easeOutQuart',
        delay: (ctx) => (ctx.type === 'data' && ctx.mode === 'default') ? ctx.dataIndex * 110 : 0
      },
      plugins: { legend: { display: false } },
      scales: {
        y: {
          beginAtZero: true,
          grid: { color: 'rgba(255, 255, 255, 0.05)' }
        },
        x: { grid: { display: false } }
      }
    }
  });
}

function renderLtvCacPaybackChart(cac, ltvCurve) {
  const canvas = document.getElementById('ltvCacPaybackChart');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  if (ltvCacPaybackChartInst) ltvCacPaybackChartInst.destroy();

  const labels = ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12'];
  const cacLine = Array(12).fill(cac);
  const gArea = createVGradient(ctx, 'rgba(16, 185, 129, 0.25)', 'rgba(16, 185, 129, 0.01)', 240);

  ltvCacPaybackChartInst = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [
        {
          label: 'Cumulative Net LTV (₹)',
          data: ltvCurve,
          borderColor: '#10B981',
          backgroundColor: gArea,
          fill: true,
          tension: 0.35,
          borderWidth: 2.5,
          pointRadius: 4,
          pointHoverRadius: 7,
          pointBackgroundColor: '#10B981',
          pointHoverBackgroundColor: '#34D399'
        },
        {
          label: 'Blended Merchant CAC (₹)',
          data: cacLine,
          borderColor: '#F43F5E',
          borderDash: [5, 5],
          borderWidth: 2,
          pointRadius: 0,
          fill: false
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      animation: {
        duration: 1200,
        easing: 'easeOutQuart'
      },
      onHover: (event, elements) => {
        const monthEl = document.getElementById('ltv-hud-month');
        const valEl = document.getElementById('ltv-hud-val');
        const profitEl = document.getElementById('ltv-hud-profit');
        const breakEl = document.getElementById('ltv-hud-breakeven');

        if (elements.length > 0) {
          const idx = elements[0].index;
          const monthNum = idx + 1;
          const ltvVal = ltvCurve[idx];
          const netMargin = ltvVal - cac;
          const roiMult = (ltvVal / cac).toFixed(2);

          monthEl.innerText = `MONTH ${monthNum} COHORT PERFORMANCE READOUT`;
          valEl.innerText = `Cum. LTV: ₹${ltvVal.toFixed(2)} vs CAC: ₹${cac.toFixed(2)} (${roiMult}x ROI)`;

          if (netMargin >= 0) {
            profitEl.innerText = `+₹${netMargin.toFixed(2)} (Profitable)`;
            profitEl.className = 'font-bold text-brandEmerald';
            breakEl.innerText = `Month ${monthNum} &ge; Breakeven`;
          } else {
            profitEl.innerText = `-₹${Math.abs(netMargin).toFixed(2)} (Payback In Progress)`;
            profitEl.className = 'font-bold text-brandRose';
            breakEl.innerText = `Payback Month ${monthNum}/12`;
          }
        }
      },
      plugins: {
        legend: {
          position: 'top',
          labels: { boxWidth: 12, font: { size: 11 } }
        },
        tooltip: {
          callbacks: {
            label: ctx => `${ctx.dataset.label}: ₹${ctx.raw.toFixed(2)}`
          }
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          grid: { color: 'rgba(255, 255, 255, 0.05)' },
          ticks: { callback: v => '₹' + v }
        },
        x: { grid: { display: false } }
      }
    }
  });
}

// -----------------------------------------------------------------------------
// 7. TAB 6: AUDIENCE BUBBLE MATRIX (WITH REAL-TIME RETICLE HUD)
// -----------------------------------------------------------------------------
let currentBubbleFilter = 'all';

function filterBubbleChart(filter) {
  currentBubbleFilter = filter;
  ['all', 'stable', 'volatile'].forEach(f => {
    const btn = document.getElementById(`btn-bubble-${f}`);
    if (btn) {
      if (f === filter) {
        btn.className = 'chart-view-btn active px-3 py-1.5 rounded-lg transition-all';
      } else {
        btn.className = 'chart-view-btn px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition-all';
      }
    }
  });
  renderAudienceBubbleChart();
}

function renderAudienceBubbleChart() {
  const canvas = document.getElementById('audienceBubbleChart');
  if (!canvas || !DASHBOARD_DATA) return;
  const ctx = canvas.getContext('2d');

  const rawAudience = DASHBOARD_DATA.audience_segments || [];
  
  let bubblePoints = rawAudience.map((seg, i) => {
    const age = seg.age || '30-34';
    const clicks = seg.clicks || (50 + i * 200);
    const cost = seg.cost_per_approved || (20 + (i % 5) * 12);
    const spend = seg.spend || (clicks * 1.5);
    return {
      x: clicks,
      y: cost,
      r: Math.min(24, Math.max(6, Math.sqrt(spend / 12))),
      ageGroup: age,
      gender: seg.gender || 'M',
      spend: spend,
      segmentId: `SEG-INT-${15 + i}`
    };
  });

  if (currentBubbleFilter === 'stable') {
    bubblePoints = bubblePoints.filter(p => p.x >= 50);
  } else if (currentBubbleFilter === 'volatile') {
    bubblePoints = bubblePoints.filter(p => p.x < 25);
  }

  if (audienceBubbleChartInst) audienceBubbleChartInst.destroy();

  audienceBubbleChartInst = new Chart(ctx, {
    type: 'bubble',
    data: {
      datasets: [
        {
          label: 'Age 30-34',
          data: bubblePoints.filter(p => p.ageGroup === '30-34'),
          backgroundColor: 'rgba(56, 189, 248, 0.7)',
          borderColor: '#38BDF8',
          borderWidth: 1.5
        },
        {
          label: 'Age 35-39',
          data: bubblePoints.filter(p => p.ageGroup === '35-39'),
          backgroundColor: 'rgba(16, 185, 129, 0.7)',
          borderColor: '#34D399',
          borderWidth: 1.5
        },
        {
          label: 'Age 40-44',
          data: bubblePoints.filter(p => p.ageGroup === '40-44'),
          backgroundColor: 'rgba(245, 158, 11, 0.7)',
          borderColor: '#FBBF24',
          borderWidth: 1.5
        },
        {
          label: 'Age 45-49',
          data: bubblePoints.filter(p => p.ageGroup === '45-49'),
          backgroundColor: 'rgba(244, 63, 94, 0.7)',
          borderColor: '#FB7185',
          borderWidth: 1.5
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      animation: {
        duration: 1000,
        easing: 'easeOutQuart'
      },
      onHover: (event, elements) => {
        const cohortEl = document.getElementById('bubble-hud-cohort');
        const valEl = document.getElementById('bubble-hud-val');
        const spendEl = document.getElementById('bubble-hud-spend');
        const classEl = document.getElementById('bubble-hud-class');

        if (elements.length > 0) {
          const dsIdx = elements[0].datasetIndex;
          const dataIdx = elements[0].index;
          const p = audienceBubbleChartInst.data.datasets[dsIdx].data[dataIdx];

          cohortEl.innerText = `${p.segmentId} | AGE ${p.ageGroup} (${p.gender})`;
          valEl.innerText = `Traffic: ${p.x} Clicks | Cost per Approved: $${p.y.toFixed(2)}`;
          spendEl.innerText = `$${p.spend.toFixed(2)}`;

          if (p.x >= 50) {
            classEl.innerText = 'Stable Core (>= 50 Clicks)';
            classEl.className = 'font-bold text-brandEmerald';
          } else if (p.x >= 25) {
            classEl.innerText = 'Moderate (25-49 Clicks)';
            classEl.className = 'font-bold text-brandCyan';
          } else {
            classEl.innerText = 'High Risk / Volatile (< 25 Clicks)';
            classEl.className = 'font-bold text-brandRose';
          }
        }
      },
      plugins: {
        legend: { position: 'top', labels: { boxWidth: 12 } },
        tooltip: {
          callbacks: {
            label: function(ctx) {
              const p = ctx.raw;
              return `${p.segmentId} (${p.ageGroup}): ${p.x} Clicks, CPA: $${p.y.toFixed(2)}, Spend: $${p.spend.toFixed(0)}`;
            }
          }
        }
      },
      scales: {
        x: {
          title: { display: true, text: 'Click Volume (Scale)', color: '#94A3B8' },
          grid: { color: 'rgba(255, 255, 255, 0.05)' }
        },
        y: {
          title: { display: true, text: 'Cost per Approved ($)', color: '#94A3B8' },
          grid: { color: 'rgba(255, 255, 255, 0.05)' },
          ticks: { callback: v => '$' + v }
        }
      }
    }
  });
}

// -----------------------------------------------------------------------------
// 8. TAB 7: LIVE A/B TESTING LAB (BELL CURVES & LASER CROSSHAIR)
// -----------------------------------------------------------------------------
function loadScenario(preset) {
  if (preset === 'real-data') {
    document.getElementById('ab-n1').value = 1984;
    document.getElementById('ab-x1').value = 183;
    document.getElementById('ab-n2').value = 36068;
    document.getElementById('ab-x2').value = 872;
    document.getElementById('ab-alpha').value = '0.05';
  } else if (preset === 'exp-001') {
    document.getElementById('ab-n1').value = 5000;
    document.getElementById('ab-x1').value = 120;
    document.getElementById('ab-n2').value = 5000;
    document.getElementById('ab-x2').value = 150;
    document.getElementById('ab-alpha').value = '0.05';
  } else if (preset === 'marginal') {
    document.getElementById('ab-n1').value = 1000;
    document.getElementById('ab-x1').value = 50;
    document.getElementById('ab-n2').value = 1000;
    document.getElementById('ab-x2').value = 52;
    document.getElementById('ab-alpha').value = '0.05';
  }
  calculateLiveAB();
}

function calculateLiveAB() {
  const n1 = parseInt(document.getElementById('ab-n1').value) || 100;
  const x1 = parseInt(document.getElementById('ab-x1').value) || 0;
  const n2 = parseInt(document.getElementById('ab-n2').value) || 100;
  const x2 = parseInt(document.getElementById('ab-x2').value) || 0;
  const alpha = parseFloat(document.getElementById('ab-alpha').value) || 0.05;

  const p1 = x1 / n1;
  const p2 = x2 / n2;
  const delta = p2 - p1;
  const lift = p1 > 0 ? (delta / p1) * 100 : 0;

  const pPool = (x1 + x2) / (n1 + n2);
  const sePool = Math.sqrt(pPool * (1 - pPool) * (1 / n1 + 1 / n2));
  const zScore = sePool > 0 ? delta / sePool : 0;
  const pValue = 2 * (1 - normalCdf(Math.abs(zScore)));

  const zCrit = alpha === 0.01 ? 2.576 : (alpha === 0.10 ? 1.645 : 1.96);
  const seDiff = Math.sqrt((p1 * (1 - p1)) / n1 + (p2 * (1 - p2)) / n2);
  const ciLower = (delta - zCrit * seDiff) * 100;
  const ciUpper = (delta + zCrit * seDiff) * 100;

  const liftEl = document.getElementById('ab-out-lift');
  liftEl.innerText = (lift >= 0 ? '+' : '') + lift.toFixed(2) + '%';
  liftEl.className = 'text-base font-bold ' + (lift >= 0 ? 'text-brandEmerald' : 'text-brandRose');

  document.getElementById('ab-out-zscore').innerText = zScore.toFixed(2);
  document.getElementById('ab-out-pvalue').innerText = pValue < 0.0001 ? '< 0.0001' : pValue.toFixed(4);
  
  const power = Math.min(100, Math.max(10, Math.round(normalCdf(Math.abs(zScore) - 1.96) * 100)));
  document.getElementById('ab-out-power').innerText = (power >= 80 ? '> ' : '') + power + '%';

  document.getElementById('ab-ci-text').innerText = `${((1 - alpha) * 100).toFixed(0)}% CI: [${ciLower.toFixed(2)}%, ${ciUpper.toFixed(2)}%]`;

  const decisionCard = document.getElementById('ab-decision-card');
  const decisionText = document.getElementById('ab-decision-text');
  const decisionIcon = document.getElementById('ab-decision-icon');

  if (pValue < alpha) {
    if (delta > 0) {
      decisionCard.className = 'p-3.5 rounded-xl border border-emerald-900/60 bg-emerald-950/20 text-emerald-300 flex items-center justify-between';
      decisionText.innerText = 'Decision: Ship & Scale (Statistically Significant Lift)';
      decisionIcon.setAttribute('data-lucide', 'check-circle-2');
    } else {
      decisionCard.className = 'p-3.5 rounded-xl border border-rose-900/60 bg-rose-950/20 text-rose-300 flex items-center justify-between';
      decisionText.innerText = 'Decision: Kill Variant (Statistically Significant Degradation)';
      decisionIcon.setAttribute('data-lucide', 'x-circle');
    }
  } else {
    decisionCard.className = 'p-3.5 rounded-xl border border-amber-900/60 bg-amber-950/20 text-amber-300 flex items-center justify-between';
    decisionText.innerText = 'Decision: Inconclusive (Insufficient Power / Null Not Rejected)';
    decisionIcon.setAttribute('data-lucide', 'help-circle');
  }

  if (window.lucide) lucide.createIcons();

  // Draw Bell Curves on Canvas
  drawBellCurves(p1, Math.max(0.001, Math.sqrt((p1 * (1 - p1)) / n1)), p2, Math.max(0.001, Math.sqrt((p2 * (1 - p2)) / n2)));
}

function normalCdf(z) {
  const t = 1 / (1 + 0.2316419 * Math.abs(z));
  const d = 0.3989423 * Math.exp(-z * z / 2);
  const prob = d * t * (0.3193815 + t * (-0.3565638 + t * (1.781478 + t * (-1.821256 + t * 1.330274))));
  return z > 0 ? 1 - prob : prob;
}

let lastBellCurveState = { mu1: 0.092, sig1: 0.006, mu2: 0.024, sig2: 0.001 };
let laserCursorX = null;

function initBellCurveCrosshair() {
  const canvas = document.getElementById('bellCurveCanvas');
  if (!canvas) return;

  function updateLaser(clientX) {
    const rect = canvas.getBoundingClientRect();
    laserCursorX = clientX - rect.left;
    drawBellCurves(lastBellCurveState.mu1, lastBellCurveState.sig1, lastBellCurveState.mu2, lastBellCurveState.sig2, laserCursorX);
  }

  canvas.addEventListener('mousemove', (e) => {
    updateLaser(e.clientX);
  });

  canvas.addEventListener('mouseleave', () => {
    laserCursorX = null;
    drawBellCurves(lastBellCurveState.mu1, lastBellCurveState.sig1, lastBellCurveState.mu2, lastBellCurveState.sig2, null);
  });

  // Mobile Touch Scrubbing Support
  canvas.addEventListener('touchstart', (e) => {
    if (e.touches && e.touches.length > 0) {
      updateLaser(e.touches[0].clientX);
    }
  }, { passive: true });

  canvas.addEventListener('touchmove', (e) => {
    if (e.touches && e.touches.length > 0) {
      updateLaser(e.touches[0].clientX);
    }
  }, { passive: true });
}

function drawBellCurves(mu1 = 0.092, sig1 = 0.006, mu2 = 0.024, sig2 = 0.001, cursorPx = null) {
  lastBellCurveState = { mu1, sig1, mu2, sig2 };
  const canvas = document.getElementById('bellCurveCanvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  const rect = canvas.getBoundingClientRect();

  canvas.width = rect.width * dpr;
  canvas.height = rect.height * dpr;
  ctx.scale(dpr, dpr);

  const W = rect.width;
  const H = rect.height;

  ctx.clearRect(0, 0, W, H);

  const minX = Math.max(0, Math.min(mu1 - 3.5 * sig1, mu2 - 3.5 * sig2));
  const maxX = Math.max(mu1 + 3.5 * sig1, mu2 + 3.5 * sig2, 0.10);
  const rangeX = maxX - minX;

  function toScreenX(x) {
    return 40 + ((x - minX) / rangeX) * (W - 80);
  }

  function fromScreenX(px) {
    return minX + ((px - 40) / (W - 80)) * rangeX;
  }

  function gaussian(x, mu, sig) {
    if (sig <= 0) return 0;
    return (1 / (sig * Math.sqrt(2 * Math.PI))) * Math.exp(-0.5 * Math.pow((x - mu) / sig, 2));
  }

  const maxDensity = Math.max(gaussian(mu1, mu1, sig1), gaussian(mu2, mu2, sig2), 20);

  function toScreenY(y) {
    return (H - 30) - (y / maxDensity) * (H - 60);
  }

  // Draw Grid Axis
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.07)';
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(40, H - 30);
  ctx.lineTo(W - 40, H - 30);
  ctx.stroke();

  function plotCurve(mu, sig, strokeColor, fillColor) {
    ctx.beginPath();
    const steps = 140;
    ctx.moveTo(toScreenX(minX), toScreenY(0));

    for (let i = 0; i <= steps; i++) {
      const x = minX + (i / steps) * rangeX;
      const y = gaussian(x, mu, sig);
      ctx.lineTo(toScreenX(x), toScreenY(y));
    }

    ctx.lineTo(toScreenX(maxX), toScreenY(0));
    ctx.closePath();

    ctx.fillStyle = fillColor;
    ctx.fill();

    ctx.strokeStyle = strokeColor;
    ctx.lineWidth = 2;
    ctx.stroke();
  }

  // Draw Curve A in Cyan
  plotCurve(mu1, sig1, '#38BDF8', 'rgba(56, 189, 248, 0.15)');

  // Draw Curve B in Violet
  plotCurve(mu2, sig2, '#8B5CF6', 'rgba(139, 92, 246, 0.15)');

  // Ticks
  ctx.fillStyle = '#64748B';
  ctx.font = '10px JetBrains Mono, monospace';
  ctx.textAlign = 'center';

  for (let s = 0; s <= 5; s++) {
    const val = minX + (s / 5) * rangeX;
    ctx.fillText((val * 100).toFixed(1) + '%', toScreenX(val), H - 12);
  }

  // Draw Laser Crosshair if mouse is active
  if (cursorPx !== null && cursorPx >= 40 && cursorPx <= W - 40) {
    const hoveredRate = fromScreenX(cursorPx);
    const density1 = gaussian(hoveredRate, mu1, sig1);
    const density2 = gaussian(hoveredRate, mu2, sig2);
    const zHover = ((hoveredRate - mu1) / sig1).toFixed(2);

    // Laser Line
    ctx.strokeStyle = '#38BDF8';
    ctx.lineWidth = 1.5;
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(cursorPx, 10);
    ctx.lineTo(cursorPx, H - 30);
    ctx.stroke();
    ctx.setLineDash([]);

    // Glow dot on curve
    ctx.fillStyle = '#38BDF8';
    ctx.beginPath();
    ctx.arc(cursorPx, toScreenY(Math.max(density1, density2)), 4, 0, Math.PI * 2);
    ctx.fill();

    // Update Real-Time Bell HUD
    const hudVal = document.getElementById('bell-hud-val');
    if (hudVal) {
      hudVal.innerText = `Rate: ${(hoveredRate * 100).toFixed(2)}% | Z-Score: ${zHover} | Density: ${Math.max(density1, density2).toFixed(1)}`;
    }
  }
}

// -----------------------------------------------------------------------------
// 9. TAB 8: CONSUMER INTENT & SESSIONS (UCI DATASET)
// -----------------------------------------------------------------------------
function renderConsumerCharts() {
  const c1 = document.getElementById('consumerCohortChart');
  const c2 = document.getElementById('consumerTrafficChart');
  if (!c1 || !c2) return;

  const ctx1 = c1.getContext('2d');
  const ctx2 = c2.getContext('2d');

  if (consumerCohortChartInst) consumerCohortChartInst.destroy();
  if (consumerTrafficChartInst) consumerTrafficChartInst.destroy();

  const gNew = createVGradient(ctx1, 'rgba(16, 185, 129, 0.9)', 'rgba(5, 150, 105, 0.25)', 250);
  const gRet = createVGradient(ctx1, 'rgba(99, 102, 241, 0.9)', 'rgba(79, 70, 229, 0.25)', 250);

  consumerCohortChartInst = new Chart(ctx1, {
    type: 'bar',
    data: {
      labels: ['New Visitors (1,694)', 'Returning Visitors (10,551)'],
      datasets: [
        {
          label: 'Conversion Rate (%)',
          data: [24.9, 13.9],
          backgroundColor: [gNew, gRet],
          borderColor: ['#34D399', '#818CF8'],
          borderWidth: 1.5,
          borderRadius: { topLeft: 8, topRight: 8 },
          maxBarThickness: 45
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      animation: {
        duration: 1000,
        easing: 'easeOutQuart',
        delay: (ctx) => (ctx.type === 'data' && ctx.mode === 'default') ? ctx.dataIndex * 140 : 0
      },
      plugins: { legend: { display: false } },
      scales: {
        y: {
          beginAtZero: true,
          grid: { color: 'rgba(255, 255, 255, 0.05)' },
          ticks: { callback: v => v + '%' }
        },
        x: { grid: { display: false } }
      }
    }
  });

  const gLine = createVGradient(ctx2, 'rgba(139, 92, 246, 0.3)', 'rgba(139, 92, 246, 0.01)', 240);

  consumerTrafficChartInst = new Chart(ctx2, {
    type: 'line',
    data: {
      labels: ['Direct (T1)', 'Search (T2)', 'Paid Social (T3)', 'Affiliate (T4)', 'Referral (T5)'],
      datasets: [
        {
          label: 'Session Conversion Rate (%)',
          data: [15.2, 21.4, 8.8, 14.2, 19.8],
          borderColor: '#A78BFA',
          backgroundColor: gLine,
          fill: true,
          tension: 0.3,
          borderWidth: 2,
          pointRadius: 4,
          pointBackgroundColor: '#A78BFA'
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      animation: {
        duration: 1200,
        easing: 'easeOutQuart'
      },
      plugins: { legend: { display: false } },
      scales: {
        y: {
          beginAtZero: true,
          grid: { color: 'rgba(255, 255, 255, 0.05)' },
          ticks: { callback: v => v + '%' }
        },
        x: { grid: { display: false } }
      }
    }
  });
}

// -----------------------------------------------------------------------------
// 10. TAB 10: ICE GROWTH ROADMAP
// -----------------------------------------------------------------------------
function filterExperiments(filter) {
  ['all', 'p0', 'p1'].forEach(id => {
    const btn = document.getElementById(`exp-filter-${id}`);
    if (btn) {
      if (id === filter.toLowerCase()) {
        btn.className = 'px-3 py-1.5 rounded-lg bg-brandIndigo text-white font-semibold';
      } else {
        btn.className = 'px-3 py-1.5 rounded-lg text-slate-400 hover:text-white';
      }
    }
  });

  renderExperiments(filter);
}

function renderExperiments(filter = 'all') {
  const grid = document.getElementById('experiments-grid');
  if (!grid || !DASHBOARD_DATA) return;
  grid.innerHTML = '';

  const experiments = DASHBOARD_DATA.experiments || [];
  const filtered = experiments.filter(e => {
    if (filter === 'P0') return e.priority.includes('P0');
    if (filter === 'P1') return e.priority.includes('P1');
    return true;
  });

  filtered.forEach(exp => {
    const card = document.createElement('div');
    card.className = 'p-5 rounded-xl bg-slate-950/60 border border-white/5 flex flex-col justify-between space-y-3 hover:border-indigo-500/40 transition-all';
    card.innerHTML = `
      <div>
        <div class="flex justify-between items-start">
          <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold ${exp.priority.includes('P0') ? 'bg-rose-950 text-rose-300 border border-rose-800' : 'bg-sky-950 text-sky-300 border border-sky-800'}">
            ${exp.priority}
          </span>
          <span class="text-xs font-mono font-bold text-brandEmerald">ICE: ${exp.ice_score.toFixed(2)}</span>
        </div>
        <h4 class="font-bold text-sm text-white mt-2.5">${exp.title}</h4>
        <p class="text-xs text-slate-400 mt-1 leading-relaxed">${exp.hypothesis}</p>
      </div>

      <div class="space-y-1.5 text-[11px] font-mono border-t border-white/5 pt-3 text-slate-300">
        <div class="flex justify-between"><span class="text-slate-500">Primary KPI:</span><span class="text-brandCyan font-bold">${exp.primary_kpi}</span></div>
        <div class="flex justify-between"><span class="text-slate-500">Guardrail:</span><span class="text-brandAmber">${exp.guardrail}</span></div>
      </div>
    `;
    grid.appendChild(card);
  });
}

// -----------------------------------------------------------------------------
// 11. TAB 11: QUALITY AUDIT RETRO TERMINAL
// -----------------------------------------------------------------------------
function renderQualityAuditTerminal() {
  const terminal = document.getElementById('terminal-logs');
  if (!terminal) return;

  const logs = [
    { rule: 'RULE_01', desc: 'Dataset Non-Empty & Row Integrity Check', status: 'PASS', metrics: '1,143 ad sets | 12,330 sessions' },
    { rule: 'RULE_02', desc: 'Primary Key Uniqueness (ad_id, session_id)', status: 'PASS', metrics: '0 duplicate keys' },
    { rule: 'RULE_03', desc: 'Zero & Negative Value Boundaries (Impressions, Spend)', status: 'PASS', metrics: 'All spend & impressions &ge; 0' },
    { rule: 'RULE_04', desc: 'Denominators Safe Divide Validation (Zero Div Guard)', status: 'PASS', metrics: '0 division errors in pipeline' },
    { rule: 'RULE_05', desc: 'Logical Funnel Monotonicity (Clicks &le; Impressions)', status: 'PASS', metrics: 'No impossible click events' },
    { rule: 'RULE_06', desc: 'Zero-Click Ad Spend Quarantine Audit', status: 'ALERT', metrics: '63 ad sets quarantined ($112.50 isolated)' },
    { rule: 'RULE_07', desc: 'Conversion Qualification Consistency (Approved &le; Total)', status: 'PASS', metrics: 'Zero approved &gt; total anomalies' },
    { rule: 'RULE_08', desc: 'Missing Categorical & Null Value Audits', status: 'ALERT', metrics: '29 null revenue sessions filtered' },
    { rule: 'RULE_09', desc: 'Audience Click Threshold Stability Checks', status: 'PASS', metrics: 'Sensitivity cuts at 10, 25, 50 clicks' },
    { rule: 'RULE_10', desc: 'Continuous 3-Factor Decomposition Identity', status: 'PASS', metrics: 'Reconciliation error = $0.00000000' },
    { rule: 'RULE_11', desc: 'Statistical Engine Boundary & CI Coverage', status: 'PASS', metrics: '25 pytest unit tests passing cleanly' }
  ];

  terminal.innerHTML = logs.map(l => `
    <div class="flex items-center justify-between text-[11px] font-mono hover:bg-slate-900/50 py-0.5 px-1 rounded">
      <div class="flex items-center space-x-2">
        <span class="text-brandCyan font-bold">[${l.rule}]</span>
        <span class="text-slate-300">${l.desc}</span>
      </div>
      <div class="flex items-center space-x-3">
        <span class="text-slate-500">${l.metrics}</span>
        <span class="font-bold px-1.5 py-0.5 rounded text-[10px] ${l.status === 'PASS' ? 'bg-emerald-950 text-brandEmerald' : 'bg-amber-950 text-brandAmber'}">${l.status}</span>
      </div>
    </div>
  `).join('');
}

// -----------------------------------------------------------------------------
// 12. STANDALONE FALLBACK PAYLOAD
// -----------------------------------------------------------------------------
function getFallbackData() {
  return {
    scorecard: [
      { campaign_id: 916, total_ads: 54, total_impressions: 482925, total_clicks: 113, total_spend: 148.52, approved_conversions: 24, ctr: 0.000234, cpm: 0.308, click_to_approved_conv_rate: 0.2124, cost_per_approved_conv: 6.19 },
      { campaign_id: 936, total_ads: 225, total_impressions: 8143820, total_clicks: 1984, total_spend: 2893.37, approved_conversions: 183, ctr: 0.000244, cpm: 0.356, click_to_approved_conv_rate: 0.0922, cost_per_approved_conv: 15.81 },
      { campaign_id: 1178, total_ads: 625, total_impressions: 204823716, total_clicks: 36068, total_spend: 55662.15, approved_conversions: 872, ctr: 0.000176, cpm: 0.272, click_to_approved_conv_rate: 0.0242, cost_per_approved_conv: 63.83 }
    ],
    decomposition: {
      base_campaign_id: 936,
      target_campaign_id: 1178,
      cost_gap: 48.02,
      lever_1_cpm_effect: -3.74,
      lever_2_ctr_effect: 4.66,
      lever_3_conv_effect: 47.10,
      reconciliation_error: 0.0
    },
    experiments: [
      { priority: 'P0 (Immediate Sprint)', title: 'Ad Creative Value Prop Realignment for Scaled Campaigns', hypothesis: 'Replace generic broad reach hooks with high-intent operational pain points to filter low-intent clicks.', primary_kpi: 'Click-to-Approved Rate (>= 3.0%)', guardrail: 'CTR >= 0.012%', ice_score: 8.67 },
      { priority: 'P0 (Immediate Sprint)', title: 'Audience Concentration in Stable High-Volume Interests', hypothesis: 'Reallocate budget from volatile <10 click interest groups to proven stable categories (IDs 16, 27).', primary_kpi: 'Cost per Approved (<= $35)', guardrail: 'Impressions >= 85%', ice_score: 8.67 },
      { priority: 'P0 (Immediate Sprint)', title: 'Post-Click Landing Form Friction Reduction & Micro-Commitment', hypothesis: 'Replace single 5-field form with 2-step progressive commitment to reduce 92.6% bounce rate.', primary_kpi: 'Click-to-Enquiry Rate (>= 12%)', guardrail: 'Lead Quality >= 30%', ice_score: 8.00 },
      { priority: 'P1 (Next Sprint)', title: 'Returning Visitor Personalized High-Intent Nudge', hypothesis: 'Deploy personalized cart/ledger nudges for returning users with high browsing duration.', primary_kpi: 'Session-to-Purchase Rate', guardrail: 'Bounce Rate <= +2%', ice_score: 7.00 },
      { priority: 'P1 (Next Sprint)', title: 'Demographic Gender-Specific Creative Framing Test', hypothesis: 'Deploy localized SMB imagery tailored to female business owner demographic cohorts.', primary_kpi: 'Post-Click Approved Rate', guardrail: 'CPC <= +10%', ice_score: 7.00 }
    ],
    audience_segments: [
      { age: '30-34', gender: 'M', clicks: 1250, cost_per_approved: 22.4, spend: 3500 },
      { age: '30-34', gender: 'F', clicks: 890, cost_per_approved: 19.8, spend: 2400 },
      { age: '35-39', gender: 'M', clicks: 2100, cost_per_approved: 32.1, spend: 5800 },
      { age: '35-39', gender: 'F', clicks: 1450, cost_per_approved: 28.6, spend: 4200 },
      { age: '40-44', gender: 'M', clicks: 1800, cost_per_approved: 48.9, spend: 6900 },
      { age: '40-44', gender: 'F', clicks: 950, cost_per_approved: 44.2, spend: 3800 },
      { age: '45-49', gender: 'M', clicks: 2400, cost_per_approved: 78.5, spend: 12400 },
      { age: '45-49', gender: 'F', clicks: 1100, cost_per_approved: 71.3, spend: 6100 }
    ]
  };
}


// -----------------------------------------------------------------------------
// NEW TAB: GROWTH OS
// -----------------------------------------------------------------------------
function renderGrowthOS() {
  const container = document.getElementById('growth-os-container');
  if (!container || !DASHBOARD_DATA || !DASHBOARD_DATA.growth_os) return;

  container.innerHTML = DASHBOARD_DATA.growth_os.map(exp => {
    // Determine priority color
    const pColor = exp.priority === 'P0' 
      ? 'bg-rose-950/80 text-rose-300 border-rose-500/30'
      : 'bg-amber-950/80 text-amber-300 border-amber-500/30';
      
    const iceColor = 'bg-indigo-950/80 text-indigo-300 border-indigo-500/30';

    return `
      <div class="designer-card rounded-xl p-4 sm:p-5 flex flex-col space-y-4">
        <div class="flex justify-between items-start gap-2">
          <div>
            <span class="inline-block px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-slate-900 border border-white/10 text-slate-400 mb-2">
              ${exp.experiment_id}
            </span>
            <h3 class="text-sm sm:text-base font-bold text-white leading-snug">${exp.title}</h3>
          </div>
          <div class="flex flex-col items-end gap-1.5 shrink-0">
            <span class="inline-block px-2 py-0.5 rounded text-[10px] font-mono font-bold ${pColor}">${exp.priority}</span>
            <span class="inline-block px-2 py-0.5 rounded text-[10px] font-mono font-bold ${iceColor}">ICE: ${exp.ice_score}</span>
          </div>
        </div>

        <!-- Stage Tabs -->
        <div class="flex items-center space-x-1.5 overflow-x-auto pb-2 custom-scrollbar border-b border-white/10">
          <button onclick="switchGrowthOsStage('${exp.experiment_id}', 'observe')" class="growth-os-tab-${exp.experiment_id} active px-3 py-1.5 min-h-[36px] rounded-lg text-[11px] font-semibold flex items-center gap-1.5 whitespace-nowrap bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 transition-all">
            <i data-lucide="eye" class="w-3.5 h-3.5"></i> <span>Observe</span>
          </button>
          <button onclick="switchGrowthOsStage('${exp.experiment_id}', 'diagnose')" class="growth-os-tab-${exp.experiment_id} px-3 py-1.5 min-h-[36px] rounded-lg text-[11px] font-semibold flex items-center gap-1.5 whitespace-nowrap text-slate-400 hover:text-white border border-transparent transition-all">
            <i data-lucide="search" class="w-3.5 h-3.5"></i> <span>Diagnose</span>
          </button>
          <button onclick="switchGrowthOsStage('${exp.experiment_id}', 'hypothesize')" class="growth-os-tab-${exp.experiment_id} px-3 py-1.5 min-h-[36px] rounded-lg text-[11px] font-semibold flex items-center gap-1.5 whitespace-nowrap text-slate-400 hover:text-white border border-transparent transition-all">
            <i data-lucide="lightbulb" class="w-3.5 h-3.5"></i> <span>Hypothesize</span>
          </button>
          <button onclick="switchGrowthOsStage('${exp.experiment_id}', 'experiment')" class="growth-os-tab-${exp.experiment_id} px-3 py-1.5 min-h-[36px] rounded-lg text-[11px] font-semibold flex items-center gap-1.5 whitespace-nowrap text-slate-400 hover:text-white border border-transparent transition-all">
            <i data-lucide="flask-conical" class="w-3.5 h-3.5"></i> <span>Experiment</span>
          </button>
          <button onclick="switchGrowthOsStage('${exp.experiment_id}', 'learn')" class="growth-os-tab-${exp.experiment_id} px-3 py-1.5 min-h-[36px] rounded-lg text-[11px] font-semibold flex items-center gap-1.5 whitespace-nowrap text-slate-400 hover:text-white border border-transparent transition-all">
            <i data-lucide="graduation-cap" class="w-3.5 h-3.5"></i> <span>Learn</span>
          </button>
        </div>

        <!-- Stage Content -->
        <div class="relative overflow-hidden min-h-[120px]">
          <div id="content-${exp.experiment_id}-observe" class="growth-os-content-${exp.experiment_id} absolute inset-0 transition-all duration-300 opacity-100 translate-x-0">
            <p class="text-xs text-slate-300 leading-relaxed">${exp.stages.observe.content}</p>
          </div>
          <div id="content-${exp.experiment_id}-diagnose" class="growth-os-content-${exp.experiment_id} absolute inset-0 transition-all duration-300 opacity-0 translate-x-4 pointer-events-none">
            <p class="text-xs text-slate-300 leading-relaxed">${exp.stages.diagnose.content}</p>
          </div>
          <div id="content-${exp.experiment_id}-hypothesize" class="growth-os-content-${exp.experiment_id} absolute inset-0 transition-all duration-300 opacity-0 translate-x-4 pointer-events-none">
            <p class="text-xs text-slate-300 leading-relaxed mb-2">${exp.stages.hypothesize.content}</p>
            <div class="p-2.5 rounded-lg bg-indigo-950/30 border border-indigo-900/50 text-[11px] font-mono text-indigo-300">
              <span class="font-bold text-indigo-400">IF/THEN:</span> ${exp.stages.hypothesize.if_then}
            </div>
          </div>
          <div id="content-${exp.experiment_id}-experiment" class="growth-os-content-${exp.experiment_id} absolute inset-0 transition-all duration-300 opacity-0 translate-x-4 pointer-events-none">
            <div class="space-y-2 text-[11px]">
              <div class="flex gap-2"><span class="text-slate-500 w-16 shrink-0">Control:</span> <span class="text-slate-300">${exp.stages.experiment.control}</span></div>
              <div class="flex gap-2"><span class="text-slate-500 w-16 shrink-0">Variant:</span> <span class="text-slate-300">${exp.stages.experiment.variant}</span></div>
              <div class="flex gap-2"><span class="text-slate-500 w-16 shrink-0">KPI:</span> <span class="text-brandCyan font-mono">${exp.stages.experiment.primary_kpi}</span></div>
              <div class="flex gap-2"><span class="text-slate-500 w-16 shrink-0">Sample:</span> <span class="text-brandEmerald font-mono">${exp.stages.experiment.sample_size_needed}</span></div>
            </div>
          </div>
          <div id="content-${exp.experiment_id}-learn" class="growth-os-content-${exp.experiment_id} absolute inset-0 transition-all duration-300 opacity-0 translate-x-4 pointer-events-none">
            <div class="space-y-2 text-[11px]">
              <div class="flex gap-2"><span class="text-slate-500 w-20 shrink-0">Success:</span> <span class="text-emerald-400">${exp.stages.learn.success_criteria}</span></div>
              <div class="flex gap-2"><span class="text-slate-500 w-20 shrink-0">Guardrail:</span> <span class="text-rose-400">${exp.stages.learn.guardrail}</span></div>
              <div class="flex gap-2"><span class="text-slate-500 w-20 shrink-0">Next Step:</span> <span class="text-slate-300">${exp.stages.learn.next_hypothesis}</span></div>
            </div>
          </div>
        </div>
      </div>
    `;
  }).join('');

  if (window.lucide) window.lucide.createIcons();
}

window.switchGrowthOsStage = function(expId, stage) {
  // Update Tabs
  document.querySelectorAll(`.growth-os-tab-${expId}`).forEach(el => {
    el.classList.remove('active', 'bg-indigo-500/20', 'text-indigo-300', 'border-indigo-500/30');
    el.classList.add('text-slate-400', 'hover:text-white', 'border-transparent');
  });
  const activeTab = event.currentTarget;
  activeTab.classList.remove('text-slate-400', 'hover:text-white', 'border-transparent');
  activeTab.classList.add('active', 'bg-indigo-500/20', 'text-indigo-300', 'border-indigo-500/30');

  // Update Content
  document.querySelectorAll(`.growth-os-content-${expId}`).forEach(el => {
    el.classList.remove('opacity-100', 'translate-x-0');
    el.classList.add('opacity-0', 'translate-x-4', 'pointer-events-none');
  });
  const activeContent = document.getElementById(`content-${expId}-${stage}`);
  if (activeContent) {
    activeContent.classList.remove('opacity-0', 'translate-x-4', 'pointer-events-none');
    activeContent.classList.add('opacity-100', 'translate-x-0');
  }
};

// -----------------------------------------------------------------------------
// NEW TAB: MARKET INTELLIGENCE
// -----------------------------------------------------------------------------
function renderMarketIntel() {
  const container = document.getElementById('market-intel-container');
  if (!container || !DASHBOARD_DATA || !DASHBOARD_DATA.market_intelligence) return;
  const data = DASHBOARD_DATA.market_intelligence;

  let html = '';

  // Section 1: Indian MSME Landscape
  if (data.msme_landscape && data.msme_landscape.metrics) {
    html += `
      <div class="space-y-3">
        <h3 class="text-sm font-bold text-white">Indian MSME Landscape</h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-3 sm:gap-4">
          ${data.msme_landscape.metrics.map(m => `
            <div class="p-4 rounded-xl bg-slate-900/60 border border-white/5 relative group">
              <h4 class="text-xl font-extrabold text-brandCyan font-mono">${m.value}</h4>
              <p class="text-xs text-slate-400 mt-1">${m.label}</p>
              <div class="absolute top-2 right-2 text-slate-500 cursor-help" title="Source: ${m.source}">
                <i data-lucide="info" class="w-3.5 h-3.5"></i>
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }

  // Section 2: Competitor Matrix
  if (data.competitor_matrix) {
    html += `
      <div class="space-y-3 pt-4 border-t border-white/10">
        <h3 class="text-sm font-bold text-white">Competitor Positioning Matrix</h3>
        <div class="overflow-x-auto custom-scrollbar">
          <table class="w-full text-left text-xs whitespace-nowrap">
            <thead>
              <tr class="border-b border-white/10 text-slate-400 font-semibold bg-slate-950/40">
                <th class="p-3">Company</th>
                <th class="p-3">Core Identity</th>
                <th class="p-3">Target Segment</th>
                <th class="p-3">Monetization</th>
                <th class="p-3">Differentiator</th>
                <th class="p-3">Status</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-white/5">
              ${data.competitor_matrix.map(c => `
                <tr class="hover:bg-white/5 transition-colors ${c.company === 'Khatabook' ? 'border-l-2 border-l-brandIndigo bg-indigo-950/10' : ''}">
                  <td class="p-3 font-bold ${c.company === 'Khatabook' ? 'text-brandIndigo' : 'text-slate-200'}">${c.company}</td>
                  <td class="p-3 text-slate-300">${c.core_identity}</td>
                  <td class="p-3 text-slate-400">${c.target_segment}</td>
                  <td class="p-3 text-slate-400">${c.monetization}</td>
                  <td class="p-3 text-slate-400">${c.differentiator}</td>
                  <td class="p-3">
                    <span class="px-2 py-0.5 rounded text-[10px] font-bold ${
                      c.status === 'Active' ? 'bg-emerald-950/80 text-emerald-400 border border-emerald-800/50' : 'bg-slate-800 text-slate-400'
                    }">${c.status}</span>
                  </td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      </div>
    `;
  }

  // Section 3: Growth Loops
  if (data.growth_loops) {
    html += `
      <div class="space-y-3 pt-4 border-t border-white/10">
        <h3 class="text-sm font-bold text-white">Khatabook Growth Loops</h3>
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-4">
          ${data.growth_loops.map(loop => `
            <div class="p-4 rounded-xl bg-slate-900/60 border border-white/5 space-y-3">
              <div class="flex justify-between items-start">
                <div class="flex items-center gap-2">
                  <span class="w-6 h-6 flex items-center justify-center rounded-lg bg-indigo-500/20 text-brandIndigo font-bold text-xs border border-indigo-500/30">${loop.id}</span>
                  <span class="font-bold text-white text-sm">${loop.name}</span>
                </div>
                <span class="px-2 py-0.5 rounded text-[10px] font-mono bg-slate-800 text-slate-300">${loop.stage}</span>
              </div>
              <p class="text-xs text-slate-400 leading-relaxed">${loop.description}</p>
              <div class="pt-2 border-t border-white/5">
                <span class="px-2 py-1 rounded text-[10px] font-mono bg-cyan-950/50 text-brandCyan border border-cyan-900/50">${loop.key_metric}</span>
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }

  // Section 4: Strategic Implications
  if (data.strategic_implications) {
    html += `
      <div class="space-y-3 pt-4 border-t border-white/10">
        <h3 class="text-sm font-bold text-white">Strategic Implications</h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          ${data.strategic_implications.map(si => `
            <div class="p-4 rounded-xl bg-slate-900/60 border border-white/5 space-y-3 relative overflow-hidden group">
              <div class="absolute inset-0 bg-gradient-to-br from-indigo-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
              
              <div>
                <p class="text-[10px] font-bold text-slate-500 uppercase tracking-wider mb-1">Market Observation</p>
                <p class="text-xs text-slate-300 font-medium">${si.observation}</p>
              </div>
              
              <div class="text-brandCyan flex justify-center py-1 opacity-50">
                <i data-lucide="arrow-down" class="w-4 h-4"></i>
              </div>
              
              <div>
                <p class="text-[10px] font-bold text-brandCyan uppercase tracking-wider mb-1">Growth Hypothesis</p>
                <p class="text-xs text-white font-medium">${si.hypothesis}</p>
              </div>
              
              <div class="pt-2">
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-purple-950/60 text-purple-300 border border-purple-800/50 flex inline-flex items-center gap-1">
                  <i data-lucide="check-circle" class="w-3 h-3"></i> ${si.jd_relevance}
                </span>
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }

  container.innerHTML = html;

  if (window.lucide) window.lucide.createIcons();
}
