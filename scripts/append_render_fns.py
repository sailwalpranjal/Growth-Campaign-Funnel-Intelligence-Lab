import os

file_path = r"e:\Growth Campaign & Funnel Intelligence Lab\web\js\dashboard.js"

content = """

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
"""

with open(file_path, "a", encoding="utf-8") as f:
    f.write(content)
