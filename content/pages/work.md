Title: Work
Slug: work

<div class="case-study">

<div class="case-study-header">
<span class="case-number">01</span>
<div>
<h2>Tiered Multi-Factor Authentication System</h2>
<p class="case-meta">Systems Engineering Capstone &middot; 2024 &middot; SysML &middot; MagicDraw/Cameo &middot; Raspberry Pi</p>
</div>
</div>

<p class="case-section-label">Problem</p>

<p>Military and critical infrastructure systems operate across fundamentally different environments — fully connected, degraded, and isolated. Standard MFA frameworks treat authentication as a single architecture, creating a gap between Zero Trust policy intent and what can actually be deployed across operational tiers.</p>

<p class="case-section-label">Approach</p>

<ul>
<li>Defined authentication requirements across three operational tiers with distinct connectivity assumptions, latency budgets, and threat models</li>
<li>Built SysML models in MagicDraw/Cameo for each tier architecture, capturing components, interfaces, and behavioral constraints</li>
<li>Conducted a formal trade study evaluating each design against a shared set of Zero Trust-derived system requirements</li>
<li>Documented interface definitions, credential freshness tradeoffs, and failure mode analysis per tier</li>
</ul>

<p class="case-section-label">Outcome</p>

<ul>
<li>Three SysML architecture models with documented design rationale aligned to Zero Trust tenets</li>
<li>Comparative analysis demonstrating how security requirements are satisfied differently under each operational tier's constraints</li>
<li>Physical prototype (Project 02) validated Tier 1 realizability and fed two design refinements back into the formal model</li>
</ul>

</div>

<div class="case-study">

<div class="case-study-header">
<span class="case-number">02</span>
<div>
<h2>Raspberry Pi MFA Prototype</h2>
<p class="case-meta">Cyber-Physical Systems &middot; 2024 &middot; Raspberry Pi &middot; Node-RED &middot; SysML</p>
</div>
</div>

<p class="case-section-label">Problem</p>

<p>The Tier 1 MFA architecture made a critical assumption: that local credential verification under network isolation was physically realizable. The SysML model could not be considered complete until that assumption was validated at the hardware level.</p>

<p class="case-section-label">Approach</p>

<ul>
<li>Implemented Tier 1 authentication logic on Raspberry Pi hardware, mapping SysML components to physical subsystems</li>
<li>Integrated Node-RED to orchestrate sensor data flow and authentication event sequencing</li>
<li>Simulated network isolation conditions to test the offline credential verification path end-to-end</li>
</ul>

<p class="case-section-label">Outcome</p>

<ul>
<li>Confirmed physical realizability of the Tier 1 SysML architecture under isolated network conditions</li>
<li>Validated the interface between authentication software and hardware sensors against the formal model</li>
<li>Identified two design refinements — fed back into the SysML model to improve interface specification accuracy</li>
</ul>

</div>

<div class="case-study">

<div class="case-study-header">
<span class="case-number">03</span>
<div>
<h2>Paper Trading Web Application</h2>
<p class="case-meta">Full-Stack Engineering &middot; 2023 &middot; Django &middot; Python</p>
</div>
</div>

<p class="case-section-label">Problem</p>

<p>Building a useful trading simulation required implementing the actual system constraints of a brokerage — authentication, transaction integrity, consistent portfolio state — not just a front-end over static mock data.</p>

<p class="case-section-label">Approach</p>

<ul>
<li>Designed a data model covering users, portfolio positions, transaction history, and market data integration</li>
<li>Built authentication and session management using Django's auth framework</li>
<li>Implemented trade execution logic with live market data to enforce realistic transaction constraints</li>
</ul>

<p class="case-section-label">Outcome</p>

<ul>
<li>Fully functional web application handling authentication, trade execution, and persistent portfolio state</li>
<li>Demonstrated full-stack engineering discipline from schema design to deployed interface</li>
</ul>

</div>
