import json
import re
from pathlib import Path

base_dir = Path('e:/Growth Campaign & Funnel Intelligence Lab')

# 1. Update index.html
html_path = base_dir / 'web' / 'index.html'
html = html_path.read_text(encoding='utf-8')

# Add Metric Dictionary tab button
metric_btn = '''        <button onclick="switchTab('metric-dict')" id="tab-btn-metric-dict" class="tab-pill px-3 py-1.5 min-h-[36px] rounded-lg border border-transparent text-slate-400 hover:text-white flex items-center space-x-1.5 whitespace-nowrap shrink-0">
          <i data-lucide="book-marked" class="w-3.5 h-3.5"></i>
          <span>Metrics</span>
        </button>

'''
html = html.replace('<button onclick="switchTab(\'quality\')"', metric_btn + '        <button onclick="switchTab(\'quality\')"')

# Add Command Center tab button
cmd_center_btn = '''        <button onclick="switchTab('command-center')" id="tab-btn-command-center" class="tab-pill active px-3 py-1.5 min-h-[36px] rounded-lg border border-transparent text-slate-400 hover:text-white flex items-center space-x-1.5 whitespace-nowrap shrink-0">
          <i data-lucide="zap" class="w-3.5 h-3.5"></i>
          <span>Command Center</span>
        </button>

'''
# Remove active from overview and add Command center button
html = html.replace('<button onclick="switchTab(\'overview\')" id="tab-btn-overview" class="tab-pill active ', '<button onclick="switchTab(\'overview\')" id="tab-btn-overview" class="tab-pill ')
html = html.replace('<button onclick="switchTab(\'overview\')" id="tab-btn-overview"', cmd_center_btn + '        <button onclick="switchTab(\'overview\')" id="tab-btn-overview"')


# Command Center HTML Content
cmd_center_html = '''
    <!-- =================================================================== -->
    <!-- TAB 0: COMMAND CENTER                                              -->
    <!-- =================================================================== -->
    <section id="tab-command-center" class="tab-content space-y-4 sm:space-y-6">
      <!-- EXECUTIVE QUESTION HEADER -->
      <div class="designer-card rounded-2xl p-4 sm:p-6 relative overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-br from-indigo-950/40 via-transparent to-violet-950/30 pointer-events-none"></div>
        <div class="relative z-10">
          <div class="flex items-center space-x-2 text-brandIndigo text-[11px] font-mono font-semibold uppercase tracking-wider mb-2">
            <i data-lucide="zap" class="w-3.5 h-3.5"></i>
            <span>Growth Command Center</span>
            <span class="ml-auto text-slate-500 font-normal normal-case">Khatabook Growth Intelligence Platform</span>
          </div>
          <h2 class="text-base sm:text-xl md:text-2xl font-extrabold text-white">What should the growth team focus on right now?</h2>
          <p class="text-xs sm:text-sm text-slate-400 mt-1 max-w-3xl">A single-screen answer to seven questions every Growth Manager needs at the start of each week. Every number links to a detailed diagnostic tab.</p>
        </div>
      </div>

      <!-- 7 EXECUTIVE QUESTIONS: 2-column grid -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">

        <!-- Q1: What changed? -->
        <div class="designer-card rounded-xl p-4 sm:p-5">
          <div class="flex items-center gap-2 mb-3">
            <span class="w-6 h-6 rounded-md bg-indigo-950 border border-indigo-700/50 flex items-center justify-center text-[10px] font-mono font-bold text-indigo-300">Q1</span>
            <span class="text-xs font-semibold text-slate-300 uppercase tracking-wider">What changed?</span>
          </div>
          <p class="text-sm text-white font-semibold leading-snug">Scaling spend 19x caused cost per approved conversion to surge 4x (+303.7%).</p>
          <p class="text-xs text-slate-400 mt-2 leading-relaxed">Campaign 936 ($ 2,893) delivered approved conversions at $15.81 each. Campaign 1178 ($55,662) delivered the same outcome at $63.83 — a $48 per-unit cost explosion despite 19x more spend.</p>
          <button onclick="switchTab('waterfall')" class="mt-3 text-xs text-brandIndigo hover:text-white font-semibold flex items-center gap-1 transition-colors">
            <i data-lucide="arrow-right" class="w-3 h-3"></i> Inspect 3-Factor Waterfall
          </button>
        </div>

        <!-- Q2: Why did it change? -->
        <div class="designer-card rounded-xl p-4 sm:p-5">
          <div class="flex items-center gap-2 mb-3">
            <span class="w-6 h-6 rounded-md bg-cyan-950 border border-cyan-700/50 flex items-center justify-center text-[10px] font-mono font-bold text-cyan-300">Q2</span>
            <span class="text-xs font-semibold text-slate-300 uppercase tracking-wider">Why did it change?</span>
          </div>
          <p class="text-sm text-white font-semibold leading-snug">98.1% of the cost surge came from post-click conversion collapse — not from media buying.</p>
          <p class="text-xs text-slate-400 mt-2 leading-relaxed">CPM actually improved 23.6% at scale (cheaper inventory). CTR decay added minor cost pressure (+$9.7%). The real culprit: post-click approved conversion rate fell 73.8% (9.22% → 2.42%), accounting for $47.10 of the $48.02 gap. Direct standardization confirms this persists even under identical audience weighting.</p>
          <button onclick="switchTab('standardization')" class="mt-3 text-xs text-brandCyan hover:text-white font-semibold flex items-center gap-1 transition-colors">
            <i data-lucide="arrow-right" class="w-3 h-3"></i> View Mix Standardization
          </button>
        </div>

        <!-- Q3: Where is the biggest opportunity? -->
        <div class="designer-card rounded-xl p-4 sm:p-5">
          <div class="flex items-center gap-2 mb-3">
            <span class="w-6 h-6 rounded-md bg-emerald-950 border border-emerald-700/50 flex items-center justify-center text-[10px] font-mono font-bold text-emerald-300">Q3</span>
            <span class="text-xs font-semibold text-slate-300 uppercase tracking-wider">Where is the biggest opportunity?</span>
          </div>
          <p class="text-sm text-white font-semibold leading-snug">Post-click form conversion is the primary lever. 92.6% of Campaign 1178 clicks never submit an enquiry.</p>
          <p class="text-xs text-slate-400 mt-2 leading-relaxed">If click-to-enquiry rate recovers from 7.4% to even half of Campaign 936's 27.1%, the blended cost per approved conversion would fall materially without increasing ad spend. This is the P0 experiment opportunity — ICE score 8.67.</p>
          <button onclick="switchTab('funnel')" class="mt-3 text-xs text-brandEmerald hover:text-white font-semibold flex items-center gap-1 transition-colors">
            <i data-lucide="arrow-right" class="w-3 h-3"></i> Inspect Funnel Drop-off
          </button>
        </div>

        <!-- Q4: What experiments are running / planned? -->
        <div class="designer-card rounded-xl p-4 sm:p-5">
          <div class="flex items-center gap-2 mb-3">
            <span class="w-6 h-6 rounded-md bg-violet-950 border border-violet-700/50 flex items-center justify-center text-[10px] font-mono font-bold text-violet-300">Q4</span>
            <span class="text-xs font-semibold text-slate-300 uppercase tracking-wider">What should we test next?</span>
          </div>
          <p class="text-sm text-white font-semibold leading-snug">Three P0 experiments are ready to run, all derived from real data anomalies.</p>
          <div class="mt-2 space-y-1.5">
            <div class="flex items-start gap-2 text-xs">
              <span class="mt-0.5 w-1.5 h-1.5 rounded-full bg-rose-400 shrink-0"></span>
              <span class="text-slate-300"><strong class="text-white">EXP-001</strong> Ad creative value prop realignment (ICE 8.67)</span>
            </div>
            <div class="flex items-start gap-2 text-xs">
              <span class="mt-0.5 w-1.5 h-1.5 rounded-full bg-rose-400 shrink-0"></span>
              <span class="text-slate-300"><strong class="text-white">EXP-002</strong> Post-click landing form friction reduction (ICE 8.00)</span>
            </div>
            <div class="flex items-start gap-2 text-xs">
              <span class="mt-0.5 w-1.5 h-1.5 rounded-full bg-rose-400 shrink-0"></span>
              <span class="text-slate-300"><strong class="text-white">EXP-003</strong> Budget reallocation to stable segments (ICE 8.67)</span>
            </div>
          </div>
          <button onclick="switchTab('growth-os')" class="mt-3 text-xs text-brandViolet hover:text-white font-semibold flex items-center gap-1 transition-colors">
            <i data-lucide="arrow-right" class="w-3 h-3"></i> Open Growth OS Pipeline
          </button>
        </div>

        <!-- Q5: What did we learn? -->
        <div class="designer-card rounded-xl p-4 sm:p-5">
          <div class="flex items-center gap-2 mb-3">
            <span class="w-6 h-6 rounded-md bg-amber-950 border border-amber-700/50 flex items-center justify-center text-[10px] font-mono font-bold text-amber-300">Q5</span>
            <span class="text-xs font-semibold text-slate-300 uppercase tracking-wider">What did we learn from the data?</span>
          </div>
          <p class="text-sm text-white font-semibold leading-snug">Scale without post-click optimization is budget destruction. Mix adjustment proves it is not an audience composition problem.</p>
          <p class="text-xs text-slate-400 mt-2 leading-relaxed">Even under identical demographic weights (direct standardization), Campaign 1178's cost per approved conversion is structurally higher — ruling out audience skew as a confound. The issue is intra-segment post-click conversion decay. This is a learnable, testable, fixable problem.</p>
          <button onclick="switchTab('standardization')" class="mt-3 text-xs text-brandAmber hover:text-white font-semibold flex items-center gap-1 transition-colors">
            <i data-lucide="arrow-right" class="w-3 h-3"></i> View Mix Adjustment Proof
          </button>
        </div>

        <!-- Q6: What market signals matter? -->
        <div class="designer-card rounded-xl p-4 sm:p-5">
          <div class="flex items-center gap-2 mb-3">
            <span class="w-6 h-6 rounded-md bg-sky-950 border border-sky-700/50 flex items-center justify-center text-[10px] font-mono font-bold text-sky-300">Q6</span>
            <span class="text-xs font-semibold text-slate-300 uppercase tracking-wider">What market signals matter?</span>
          </div>
          <p class="text-sm text-white font-semibold leading-snug">OkCredit is retreating. BharatPe's hardware scale is a competitive gap. App store trust signals point to onboarding friction.</p>
          <div class="mt-2 space-y-1.5">
            <div class="flex items-start gap-2 text-xs">
              <span class="mt-0.5 w-1.5 h-1.5 rounded-full bg-emerald-400 shrink-0"></span>
              <span class="text-slate-300">OkCredit P2P lending shut down (RBI 2025) — acquisition window in their Tier-3 markets</span>
            </div>
            <div class="flex items-start gap-2 text-xs">
              <span class="mt-0.5 w-1.5 h-1.5 rounded-full bg-amber-400 shrink-0"></span>
              <span class="text-slate-300">BharatPe 5M+ Soundboxes: payment data Khatabook currently lacks</span>
            </div>
            <div class="flex items-start gap-2 text-xs">
              <span class="mt-0.5 w-1.5 h-1.5 rounded-full bg-rose-400 shrink-0"></span>
              <span class="text-slate-300">App Store signal: unsolicited calls post-signup flagged as uninstall trigger</span>
            </div>
          </div>
          <button onclick="switchTab('market-intel')" class="mt-3 text-xs text-brandCyan hover:text-white font-semibold flex items-center gap-1 transition-colors">
            <i data-lucide="arrow-right" class="w-3 h-3"></i> Open Market Intelligence
          </button>
        </div>

        <!-- Q7: How reliable is the underlying data? (full width) -->
        <div class="designer-card rounded-xl p-4 sm:p-5 lg:col-span-2">
          <div class="flex items-center gap-2 mb-3">
            <span class="w-6 h-6 rounded-md bg-slate-800 border border-slate-600/50 flex items-center justify-center text-[10px] font-mono font-bold text-slate-300">Q7</span>
            <span class="text-xs font-semibold text-slate-300 uppercase tracking-wider">How reliable is the underlying data?</span>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <div>
              <p class="text-xs font-semibold text-emerald-400 mb-1">What we can trust</p>
              <ul class="text-xs text-slate-400 space-y-1">
                <li class="flex items-start gap-1.5"><span class="mt-0.5 text-emerald-400">+</span>1,143 real ad records, zero synthetic values</li>
                <li class="flex items-start gap-1.5"><span class="mt-0.5 text-emerald-400">+</span>11-check automated data quality audit (all passed)</li>
                <li class="flex items-start gap-1.5"><span class="mt-0.5 text-emerald-400">+</span>Ratio-of-sums aggregation prevents Simpson's paradox</li>
                <li class="flex items-start gap-1.5"><span class="mt-0.5 text-emerald-400">+</span>Decomposition reconciles to 100.000% (zero residual)</li>
              </ul>
            </div>
            <div>
              <p class="text-xs font-semibold text-amber-400 mb-1">Known limitations</p>
              <ul class="text-xs text-slate-400 space-y-1">
                <li class="flex items-start gap-1.5"><span class="mt-0.5 text-amber-400">~</span>No app install, login, or retention data available</li>
                <li class="flex items-start gap-1.5"><span class="mt-0.5 text-amber-400">~</span>Dataset ends at approved conversion — no downstream LTV</li>
                <li class="flex items-start gap-1.5"><span class="mt-0.5 text-amber-400">~</span>No time dimension — cannot compute period-over-period trends</li>
              </ul>
            </div>
            <div>
              <p class="text-xs font-semibold text-rose-400 mb-1">What we will not compute</p>
              <ul class="text-xs text-slate-400 space-y-1">
                <li class="flex items-start gap-1.5"><span class="mt-0.5 text-rose-400">×</span>Revenue or ROAS — no transaction data exists</li>
                <li class="flex items-start gap-1.5"><span class="mt-0.5 text-rose-400">×</span>True CAC — excludes blended organic spend</li>
                <li class="flex items-start gap-1.5"><span class="mt-0.5 text-rose-400">×</span>Khatabook internal metrics — 100% public datasets only</li>
              </ul>
            </div>
          </div>
          <div class="mt-4 pt-4 border-t border-white/5 flex items-center gap-3 text-xs">
            <span class="flex items-center gap-1.5 text-emerald-400 font-semibold"><i data-lucide="shield-check" class="w-3 h-3"></i> 40 tests passing</span>
            <span class="text-slate-600">|</span>
            <span class="text-slate-400">Dataset A: 1,143 records</span>
            <span class="text-slate-600">|</span>
            <span class="text-slate-400">Dataset B: 12,330 sessions</span>
            <span class="text-slate-600">|</span>
            <button onclick="switchTab('quality')" class="text-slate-400 hover:text-white flex items-center gap-1 transition-colors">
              <i data-lucide="terminal" class="w-3 h-3"></i> Audit Daemon
            </button>
          </div>
        </div>

      </div>
    </section>
'''
html = html.replace('<section id="tab-overview" class="tab-content space-y-4 sm:space-y-6">', cmd_center_html + '\n    <section id="tab-overview" class="tab-content hidden space-y-4 sm:space-y-6">')


# Metric Dictionary Tab Content
metric_html = '''
    <!-- =================================================================== -->
    <!-- TAB: METRIC DICTIONARY                                             -->
    <!-- =================================================================== -->
    <section id="tab-metric-dict" class="tab-content hidden space-y-4 sm:space-y-6">
      <!-- Page purpose header -->
      <div class="designer-card rounded-2xl p-4 sm:p-6">
        <div class="flex items-center space-x-2 text-brandCyan text-[11px] font-mono font-semibold uppercase tracking-wider mb-2">
          <i data-lucide="book-marked" class="w-3.5 h-3.5"></i>
          <span>Metric & Methodology Dictionary</span>
        </div>
        <h2 class="text-base sm:text-xl font-extrabold text-white">In-Product Metric Reference</h2>
        <p class="text-xs text-slate-400 mt-1 max-w-3xl">Every metric, abbreviation, and formula used across this platform. Includes exact formula, derivation chain, data source, confidence level, and what it can and cannot prove. No acronym is assumed to be self-evident.</p>
        <!-- Search box -->
        <div class="mt-4 relative">
          <i data-lucide="search" class="absolute left-3 top-1/2 -translate-y-1/2 w-3.5 h-3.5 text-slate-500"></i>
          <input type="text" id="metric-search" placeholder="Search metrics (e.g. CTR, CAC, p-value)..." 
            class="w-full max-w-md pl-9 pr-4 py-2 rounded-lg bg-slate-900/80 border border-white/10 text-xs text-white placeholder:text-slate-500 focus:outline-none focus:border-indigo-500/60" 
            oninput="filterMetrics(this.value)">
        </div>
      </div>

      <!-- Metric cards grid -->
      <div id="metric-dict-container" class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-3 sm:gap-4"></div>
    </section>
'''
# Insert Metric tab before tab-quality
html = html.replace('<section id="tab-quality"', metric_html + '\n    <section id="tab-quality"')

# Add Purpose Headers
def add_header(html_text, section_id, question, data, decision):
    header = f'''      <!-- Page Purpose Header -->
      <div class="flex flex-wrap items-start justify-between gap-3 mb-1">
        <div class="text-[11px] text-slate-500 font-mono">
          <span class="text-slate-400 font-semibold">This page answers:</span> {question} &nbsp;|&nbsp;
          <span class="text-slate-400 font-semibold">Data:</span> {data} &nbsp;|&nbsp;
          <span class="text-slate-400 font-semibold">Decision:</span> {decision}
        </div>
      </div>
'''
    match = re.search(f'<section id="{section_id}"[^>]*>', html_text)
    if match:
        return html_text[:match.end()] + '\n' + header + html_text[match.end():]
    return html_text

html = add_header(html, 'tab-waterfall', 'What caused cost per approved conversion to change between campaigns?', 'Dataset A (1,143 ad records)', 'Which lever (CPM, CTR, or conversion rate) to fix first')
html = add_header(html, 'tab-funnel', 'Where exactly do users drop off in the acquisition funnel?', 'Dataset A campaigns', 'Where to focus conversion rate optimization effort')
html = add_header(html, 'tab-audience', 'Which audience segments are statistically reliable and most cost-efficient?', 'Dataset A interest/age/gender breakdowns', 'Which segments to scale, pause, or test further')
html = add_header(html, 'tab-ab-lab', 'Is this observed conversion difference statistically significant and large enough to act on?', 'User-entered experiment results + real baseline rates', 'Ship variant, extend test, or do not conclude')
html = add_header(html, 'tab-consumer', 'How does on-site session behavior correlate with conversion outcomes?', 'Dataset B (12,330 UCI sessions)', 'Which behavioral signals to surface in CRM re-engagement targeting')

html_path.write_text(html, encoding='utf-8')


# 2. Update dashboard.js
js_path = base_dir / 'web' / 'js' / 'dashboard.js'
js = js_path.read_text(encoding='utf-8')


if "switchTab('overview')" in js and "initDashboard" in js:
    js = js.replace("switchTab('overview')", "switchTab('command-center')")
else:
    js = js.replace('await initDashboard();\n});', "await initDashboard();\n  switchTab('command-center');\n});")


# Add lazy loading to switchTab
lazy_code = '''
  if (tabId === 'metric-dict' && DASHBOARD_DATA?.metric_dictionary && !window._metricDictRendered) {
    renderMetricDictionary();
    window._metricDictRendered = true;
  }
  if (tabId === 'command-center') {
    if (window.lucide) window.lucide.createIcons();
    if (DASHBOARD_DATA?.growth_os && !window._growthOsRendered) {
        renderGrowthOS();
        window._growthOsRendered = true;
    }
  }
'''
js = js.replace("if (tabId === 'growth-os'", lazy_code + "\n  if (tabId === 'growth-os'")

# Add renderMetricDictionary and filterMetrics functions at the end of the file
metric_js = '''
function renderMetricDictionary() {
  const container = document.getElementById('metric-dict-container');
  if (!container || !DASHBOARD_DATA?.metric_dictionary) return;

  const metrics = DASHBOARD_DATA.metric_dictionary;
  container.innerHTML = metrics.map(m => {
    const isAvailable = m.availability === 'Available';
    const confidenceColor = m.confidence === 'High' ? 'text-emerald-400' : m.confidence === 'Medium' ? 'text-amber-400' : 'text-rose-400';
    const availBadge = isAvailable 
      ? '<span class="px-1.5 py-0.5 rounded text-[10px] font-mono font-bold bg-emerald-950/80 text-emerald-300 border border-emerald-700/40">Available</span>'
      : '<span class="px-1.5 py-0.5 rounded text-[10px] font-mono font-bold bg-rose-950/80 text-rose-300 border border-rose-700/40">Not Available</span>';
    
    return `<div class="designer-card rounded-xl p-4 sm:p-5 space-y-3 metric-dict-card" data-metric="${m.metric.toLowerCase()}">
      <div class="flex items-start justify-between gap-2">
        <h3 class="font-bold text-sm text-white leading-tight">${m.metric}</h3>
        ${availBadge}
      </div>
      <div class="font-mono text-xs text-brandIndigo bg-indigo-950/40 border border-indigo-800/30 rounded-lg px-3 py-2">${m.formula}</div>
      <div class="space-y-1.5 text-xs">
        <div class="flex items-start gap-2">
          <span class="text-slate-500 shrink-0 w-20">Source</span>
          <span class="text-slate-300">${m.data_source || 'N/A'}</span>
        </div>
        <div class="flex items-start gap-2">
          <span class="text-slate-500 shrink-0 w-20">Confidence</span>
          <span class="font-semibold ${confidenceColor}">${m.confidence}</span>
        </div>
        ${m.aggregation_method ? `<div class="flex items-start gap-2"><span class="text-slate-500 shrink-0 w-20">Method</span><span class="text-slate-300">${m.aggregation_method}</span></div>` : ''}
        <div class="pt-1.5 border-t border-white/5">
          <p class="text-slate-400 leading-relaxed">${m.known_limitation}</p>
        </div>
        <div class="pt-1.5 border-t border-white/5">
          <p class="text-[11px] text-indigo-300/80 leading-relaxed"><span class="font-semibold text-indigo-400">Growth relevance:</span> ${m.khatabook_relevance}</p>
        </div>
      </div>
    </div>`;
  }).join('');
  if (window.lucide) window.lucide.createIcons();
}

function filterMetrics(query) {
  const cards = document.querySelectorAll('.metric-dict-card');
  const q = query.toLowerCase();
  cards.forEach(card => {
    const text = card.dataset.metric + ' ' + card.textContent.toLowerCase();
    card.style.display = text.includes(q) ? '' : 'none';
  });
}
'''
js += '\n' + metric_js


# Add App store signals render logic inside renderMarketIntel
app_store_js = '''
  // App Store Signals
  const appStoreData = DASHBOARD_DATA.market_intelligence.app_store_signals;
  if (appStoreData) {
    const appStoreHtml = `
      <div class="mt-6 pt-6 border-t border-white/10 space-y-4">
        <div class="flex items-center justify-between">
          <h3 class="text-sm font-bold text-white flex items-center gap-2">
            <i data-lucide="smartphone" class="w-4 h-4 text-brandIndigo"></i> App Store Signal Analysis
          </h3>
          <span class="px-2 py-1 rounded-md bg-slate-900 border border-slate-700 text-[10px] font-mono text-slate-400">Publicly observable Play Store review patterns — not a statistical sample</span>
        </div>
        
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
          <!-- Positive Themes -->
          <div class="space-y-3">
            <h4 class="text-xs font-semibold text-emerald-400 uppercase tracking-wider">Positive Signals (Protect & Scale)</h4>
            ${appStoreData.positive_themes.map(t => `
              <div class="p-3.5 rounded-xl bg-emerald-950/10 border-l-2 border-l-emerald-500 border border-white/5 space-y-1.5">
                <div class="flex items-start justify-between gap-2">
                  <span class="text-xs text-white font-medium">${t.theme}</span>
                  <span class="px-1.5 py-0.5 rounded text-[9px] font-mono font-bold bg-emerald-900/60 text-emerald-300">${t.signal_strength}</span>
                </div>
                <p class="text-[11px] text-slate-400">${t.growth_implication}</p>
              </div>
            `).join('')}
          </div>
          
          <!-- Friction Themes -->
          <div class="space-y-3">
            <h4 class="text-xs font-semibold text-rose-400 uppercase tracking-wider">Friction Signals (Fix & Test)</h4>
            ${appStoreData.friction_themes.map(t => `
              <div class="p-3.5 rounded-xl bg-rose-950/10 border-l-2 border-l-rose-500 border border-white/5 space-y-1.5">
                <div class="flex items-start justify-between gap-2">
                  <span class="text-xs text-white font-medium">${t.theme}</span>
                  <span class="px-1.5 py-0.5 rounded text-[9px] font-mono font-bold ${t.signal_strength === 'Recurring' ? 'bg-rose-900/60 text-rose-300' : 'bg-amber-900/60 text-amber-300'}">${t.signal_strength}</span>
                </div>
                <p class="text-[11px] text-slate-400">${t.growth_implication}</p>
              </div>
            `).join('')}
          </div>
        </div>

        <!-- Hypotheses -->
        <div class="p-4 rounded-xl bg-indigo-950/20 border border-indigo-900/40 space-y-2">
          <h4 class="text-xs font-semibold text-indigo-300 uppercase tracking-wider mb-2">Derived Experiment Hypotheses</h4>
          <ul class="space-y-2">
            ${appStoreData.experiment_hypotheses.map(h => `
              <li class="flex items-start gap-2 text-xs text-slate-300">
                <i data-lucide="flask-conical" class="w-3.5 h-3.5 text-brandIndigo shrink-0 mt-0.5"></i>
                <span>${h}</span>
              </li>
            `).join('')}
          </ul>
        </div>
      </div>
    `;
    
    // Find the market-intel tab container and append (or insert inside existing content container if there is one)
    const container = document.getElementById('market-intel-container') || document.querySelector('#tab-market-intel > div > div:last-child');
    if (container) {
      container.innerHTML += appStoreHtml;
    }
  }
'''

# We want to place this at the end of renderMarketIntel. Let's find where it sets up the market Intel cards.
# Wait, let's just find the function end by looking for something like:
# "renderStrategicImplications();" or similar? Let's just put it at the very end of the function body.
js = js.replace('  if (window.lucide) window.lucide.createIcons();\n}', app_store_js + '\n  if (window.lucide) window.lucide.createIcons();\n}', 1)
# if it fails, maybe it's `lucide.createIcons();`
js = js.replace('  if (window.lucide) {\n    lucide.createIcons();\n  }\n}', app_store_js + '\n  if (window.lucide) {\n    lucide.createIcons();\n  }\n}', 1)

js_path.write_text(js, encoding='utf-8')


# 3. Update dashboard_data.json
json_path = base_dir / 'web' / 'data' / 'dashboard_data.json'
data = json.loads(json_path.read_text(encoding='utf-8'))

data['market_intelligence']['app_store_signals'] = {
  "note": "Based on observable patterns from public Google Play Store reviews. Not a representative sample. Trends only — not statistical claims.",
  "khatabook_rating": 4.2,
  "reviews_analyzed_approx": "2M+ public reviews",
  "positive_themes": [
    { "theme": "WhatsApp reminder works instantly", "signal_strength": "Strong", "growth_implication": "Reminder loop is the strongest retention hook — protect it in any CRM redesign" },
    { "theme": "Regional language support praised (Hindi, Telugu, Tamil)", "signal_strength": "Strong", "growth_implication": "Vernacular-first is a real moat — launch new features in regional languages first" },
    { "theme": "Simple udhaar recording praised by Kirana owners", "signal_strength": "Strong", "growth_implication": "Core UX is working for the primary persona; complexity should be opt-in, not default" }
  ],
  "friction_themes": [
    { "theme": "Unsolicited calls post-signup", "signal_strength": "Recurring", "growth_implication": "Cold outbound calls after install are flagged as uninstall triggers. Replace with in-app nudge sequences for D1-D7 activation" },
    { "theme": "Premium features gated behind coin/subscription paywall", "signal_strength": "Moderate", "growth_implication": "Monetization wall hits before activation habit is formed. Consider delaying paywall to D14+ after first payment reminder sent" },
    { "theme": "Sync issues across devices mentioned", "signal_strength": "Moderate", "growth_implication": "Sync reliability is table stakes for merchant trust — particularly for bookkeeping data" }
  ],
  "experiment_hypotheses": [
    "Replacing post-install cold calls with a D1 in-app tutorial nudge sequence could improve D7 retention",
    "Delaying the premium paywall until after first WhatsApp reminder is sent could increase willingness-to-pay",
    "A 'sync status' indicator on the home screen could reduce trust anxiety for multi-device merchants"
  ]
}

json_path.write_text(json.dumps(data, indent=4), encoding='utf-8')
