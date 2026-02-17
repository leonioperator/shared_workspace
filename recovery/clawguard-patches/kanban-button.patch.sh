#!/bin/bash
# Reapply Kanban tab (iframe) to ClawGuard after update
CG_HTML="/usr/lib/node_modules/@jaydenbeard/clawguard/public/index.html"

if ! grep -q "tab-kanban" "$CG_HTML"; then
  # Add Kanban tab button before TokenCTL button (or before closing div of tabs)
  sed -i '/data-tab="tokenctl"/i\      <button class="tab-btn px-4 py-2 rounded-lg text-sm font-medium border border-transparent hover:bg-slate-800" data-tab="kanban">\n        📋 Kanban\n      <\/button>' "$CG_HTML"
  
  # Add Kanban tab content (iframe) before TokenCTL tab content
  sed -i '/Tab Content: TokenCTL/i\    <!-- Tab Content: Kanban -->\n    <div id="tab-kanban" class="tab-content hidden">\n      <iframe src="http:\/\/localhost:3848" style="width:100%;height:calc(100vh - 140px);border:none;border-radius:12px;background:#0f172a;"><\/iframe>\n    <\/div>\n' "$CG_HTML"
  
  echo "Kanban tab added to ClawGuard"
else
  echo "Kanban tab already present"
fi
