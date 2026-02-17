#!/bin/bash
# Reapply TokenCTL tab + iframe to ClawGuard after update
CG_HTML="/usr/lib/node_modules/@jaydenbeard/clawguard/public/index.html"

if ! grep -q "tokenctl" "$CG_HTML"; then
  # Add TokenCTL tab button before Kanban link
  sed -i '/📋 Kanban/i\      <button class="tab-btn px-4 py-2 rounded-lg text-sm font-medium border border-transparent hover:bg-slate-800" data-tab="tokenctl">\n        📊 TokenCTL\n      <\/button>' "$CG_HTML"
  
  # Add TokenCTL tab content (iframe) before Bookmarks tab content
  sed -i '/Tab Content: Bookmarks/i\    <!-- Tab Content: TokenCTL -->\n    <div id="tab-tokenctl" class="tab-content hidden">\n      <iframe src="http:\/\/localhost:3849" style="width:100%;height:calc(100vh - 140px);border:none;border-radius:12px;background:#0f172a;"><\/iframe>\n    <\/div>\n' "$CG_HTML"
  
  echo "TokenCTL tab added to ClawGuard"
else
  echo "TokenCTL tab already present"
fi
