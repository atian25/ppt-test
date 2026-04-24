import re

slides_html = """
<!-- Slide 1: 开场封面 -->
<section class="slide hero dark">
  <div class="chrome">
    <div>SOLO 0418 直播 · 天猪</div>
    <div>Act 0 · 01 / 12</div>
  </div>
  <div class="frame" style="display:grid; gap:4vh; align-content:center; min-height:80vh">
    <div class="kicker">SOLO 独立版发布</div>
    <h1 class="h-hero" style="font-size:10vw">SOLO 独立版</h1>
    <h2 class="h-sub" style="font-size:3vw; font-family:var(--serif-zh); font-weight:400; opacity:0.8">探索 AI Coding 的第三阶段：AI 自主编程</h2>
    <p class="lead" style="max-width:60vw; margin-top:2vh">
      随着大模型能力的极大提升，AI 已经从编程扩展到各个领域。今天，我们正式推出 SOLO 独立版。
    </p>
    <div class="meta-row" style="font-family:var(--mono); font-size:12px; letter-spacing:0.15em; text-transform:uppercase; opacity:0.6; margin-top:2vh">
      <span>天猪</span><span style="margin:0 1em">·</span><span>字节跳动 / SOLO 团队</span>
    </div>
  </div>
  <div class="foot">
    <div>一场关于 AI · 组织 · 个体的分享</div>
    <div>— 2026 —</div>
  </div>
</section>

<!-- Slide 2: 大字报 (个人历程) -->
<section class="slide light">
  <div class="chrome">
    <div>开场 · 闭关历程</div>
    <div>Act I · 02 / 12</div>
  </div>
  <div class="frame" style="padding-top:6vh">
    <div class="kicker">11月15日的“受难者”</div>
    <h2 class="h-xl" style="font-family:var(--serif-zh); font-weight:700; font-size:5vw; line-height:1.1; margin-bottom:6vh">
      每年 11 月 15 日的闭关传统，<br>带来了认知与工具的持续进化。
    </h2>
    <div class="grid-4">
      <div class="stat-card">
        <div class="stat-label">加入字节</div>
        <div class="stat-nb" style="font-family:var(--serif-en); font-weight:700; font-size:6vw; letter-spacing:-0.02em">2022<span class="stat-unit" style="font-size:0.4em">.11.15</span></div>
      </div>
      <div class="stat-card">
        <div class="stat-label">闭关产出</div>
        <div class="stat-nb" style="font-family:var(--serif-en); font-weight:700; font-size:6vw; letter-spacing:-0.02em">MarsCode<span class="stat-unit" style="font-size:0.4em"> Cloud IDE</span></div>
        <div class="stat-note">2023.11.15</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">闭关产出</div>
        <div class="stat-nb" style="font-family:var(--serif-en); font-weight:700; font-size:6vw; letter-spacing:-0.02em">TRAE<span class="stat-unit" style="font-size:0.4em"> IDE</span></div>
        <div class="stat-note">2024.11.15</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">全新产出</div>
        <div class="stat-nb" style="font-family:var(--serif-zh); font-weight:700; font-size:6vw; letter-spacing:-0.02em">SOLO<span class="stat-unit" style="font-size:0.4em"> 独立版</span></div>
        <div class="stat-note">2026年初 闭关</div>
      </div>
    </div>
  </div>
  <div class="foot">
    <div>认知的迭代</div>
    <div>— · —</div>
  </div>
</section>

<!-- Slide 3: 大引用 (AI 定位的演进) -->
<section class="slide dark">
  <div class="chrome">
    <div>开场 · 重新定义 AI</div>
    <div>Act I · 03 / 12</div>
  </div>
  <div class="frame" style="display:flex; flex-direction:column; justify-content:center; padding:0 8vw">
    <div class="kicker" style="margin-bottom:4vh">AI 角色跃迁</div>
    <div class="callout" style="border-left:none; padding:0; background:none">
      <div class="q-big" style="font-size:3.5vw; line-height:1.3; font-weight:500; opacity:0.95">
        从“人人都配备的高潜实习生”，到“每个人专属的<span class="hi">高级个人助理</span>”。
      </div>
      <div class="cite" style="margin-top:4vh; font-size:13px; opacity:0.7; display:flex; align-items:center; gap:1vw">
        <i class="ico ico-sm" data-lucide="arrow-right"></i> AI 能力边界认知的全面升级
      </div>
    </div>
  </div>
  <div class="foot">
    <div>AI 角色跃迁</div>
    <div>— · —</div>
  </div>
</section>

<!-- Slide 4: 对比 (认知的跃迁) -->
<section class="slide light">
  <div class="chrome">
    <div>开场 · 认知的保鲜期</div>
    <div>Act I · 04 / 12</div>
  </div>
  <div class="frame" style="padding-top:6vh; display:flex; flex-direction:column">
    <div class="kicker">痛并快乐着的打脸</div>
    <h2 class="h-xl" style="font-family:var(--serif-zh); font-weight:700; font-size:4.5vw; margin-bottom:8vh">2月份的认知，在12月份就被推翻。</h2>
    
    <div class="split" style="flex:1; align-items:start; gap:8vw">
      <!-- 左侧 -->
      <div class="col" style="gap:3vh">
        <div class="meta" style="color:rgba(0,0,0,0.4); border-bottom:1px solid rgba(0,0,0,0.1); padding-bottom:1.5vh">2月份的判断</div>
        <h3 class="h3-zh" style="font-size:2.2vw">Tab Tab 是仪式感</h3>
        <p class="body-zh">
          当时认为 Builder 只是吸引尝鲜，Tab Tab 才是过日子的惊喜感。虽然知道未来是 Agent（自主理解、调用工具、完成任务），但觉得这一天还很远。
        </p>
      </div>
      <!-- 右侧 -->
      <div class="col" style="gap:3vh">
        <div class="meta" style="color:rgba(0,0,0,0.4); border-bottom:1px solid rgba(0,0,0,0.1); padding-bottom:1.5vh">12月份的共识</div>
        <h3 class="h3-zh" style="font-size:2.2vw">AI 自主编程已成常态</h3>
        <p class="body-zh">
          用 Agent 做长时间异步并行、在严肃场景中深度使用已成共识。比如社区 Expert 全年用 Agent 写了 30 万行代码，但只 Tab Tab 了 12 次。直接进入了第三阶段。
        </p>
      </div>
    </div>
  </div>
  <div class="foot">
    <div>认知的跃迁速度</div>
    <div>— · —</div>
  </div>
</section>

<!-- Slide 5: 章节幕封 -->
<section class="slide hero light">
  <div class="chrome">
    <div>第二幕 · 真实实践</div>
    <div>Act II · 05 / 12</div>
  </div>
  <div class="frame" style="display:grid; gap:6vh; align-content:center; min-height:80vh">
    <div class="kicker">Act II</div>
    <h1 class="h-hero" style="font-size:8.5vw; font-family:var(--serif-zh); font-weight:700; letter-spacing:-0.02em">实践：SOLO Powers SOLO</h1>
    <p class="lead" style="max-width:55vw">
      在前线看到了什么？我们把自己作为最佳实践，吃自己的狗粮。
    </p>
  </div>
  <div class="foot">
    <div>基于第一线的实践经验</div>
    <div>— · —</div>
  </div>
</section>

<!-- Slide 6: 数据大字报 (吃自己的狗粮) -->
<section class="slide dark">
  <div class="chrome">
    <div>实践 · 惊人的数据</div>
    <div>Act II · 06 / 12</div>
  </div>
  <div class="frame" style="padding-top:6vh">
    <div class="kicker">开发 SOLO 的真实数据</div>
    <h2 class="h-xl" style="font-family:var(--serif-zh); font-weight:700; font-size:4.5vw; line-height:1.2; margin-bottom:8vh; max-width:70vw">
      我们不仅是做工具的人，更是第一批深度用户。
    </h2>
    <div class="grid-3">
      <div class="stat-card">
        <div class="stat-label" style="opacity:0.8">产出代码行数</div>
        <div class="stat-nb" style="font-family:var(--serif-en); font-weight:700; font-size:7vw">100<span class="stat-unit">万+</span></div>
      </div>
      <div class="stat-card">
        <div class="stat-label" style="opacity:0.8">总提交次数</div>
        <div class="stat-nb" style="font-family:var(--serif-en); font-weight:700; font-size:7vw">9,000<span class="stat-unit">+</span></div>
      </div>
      <div class="stat-card">
        <div class="stat-label" style="opacity:0.8">AI 代码贡献率</div>
        <div class="stat-nb" style="font-family:var(--serif-en); font-weight:700; font-size:7vw; color:#8ab4f8">93<span class="stat-unit">%</span></div>
        <div class="stat-note" style="color:rgba(255,255,255,0.5)">半年后可能就是整个行业的常态</div>
      </div>
    </div>
  </div>
  <div class="foot">
    <div>SOLO Powers SOLO</div>
    <div>— · —</div>
  </div>
</section>

<!-- Slide 7: 图文混排 (Good: 知识显性化) -->
<section class="slide light">
  <div class="chrome">
    <div>实践 · 积极变化</div>
    <div>Act II · 07 / 12</div>
  </div>
  <div class="frame grid-2-6-6" style="padding-top:4vh; gap:6vw">
    <!-- 左：文字 -->
    <div class="col" style="justify-content:center; gap:4vh">
      <div class="kicker">The Good Side</div>
      <h2 class="h-xl" style="font-family:var(--serif-zh); font-weight:700; font-size:4vw; line-height:1.15">知识显性化：<br>从个人到团队</h2>
      <p class="body-zh">
        我们将团队的“隐性知识”沉淀为 AI 能读懂的 Skill 文件。那些只存在老员工脑子里的模块设计取舍、隐性耦合，现在变成了 AI 可以准确执行的标准。
      </p>
      <div class="callout" style="margin-top:2vh">
        <div class="q-big" style="font-size:1.4vw">以前新人上手要问三个老员工，现在一个 Skill 文件就能让 AI 准确执行。维护成本大幅下降。</div>
      </div>
    </div>
    <!-- 右：AI 配图 -->
    <figure class="frame-img" style="height:60vh; align-self:center">
      <img src="https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=Futuristic+digital+library+glowing+nodes+connecting+explicit+knowledge+data+visualization+UI+web+design+clean+minimalist+light+theme&image_size=landscape_16_9" alt="知识显性化">
      <div class="frame-cap">
        <span class="pf">团队知识沉淀为 Skill</span>
        <span class="idx">FIG. 01</span>
      </div>
    </figure>
  </div>
  <div class="foot">
    <div>知识显性化探索</div>
    <div>— · —</div>
  </div>
</section>

<!-- Slide 8: 图文混排 (Bad: 个人速度 ≠ 组织速度) -->
<section class="slide light">
  <div class="chrome">
    <div>实践 · 真实痛点</div>
    <div>Act II · 08 / 12</div>
  </div>
  <div class="frame grid-2-6-6" style="padding-top:4vh; gap:6vw">
    <!-- 左：文字 -->
    <div class="col" style="justify-content:center; gap:4vh">
      <div class="kicker">The Bad Side</div>
      <h2 class="h-xl" style="font-family:var(--serif-zh); font-weight:700; font-size:4vw; line-height:1.15">个人速度，<br>不等于组织速度</h2>
      <p class="body-zh">
        AI 让写代码快了一个数量级，但产出量大了，Review 成为瓶颈。上下游衔接成本上升，交付周期并未同比例缩短。
      </p>
      <div class="callout" style="margin-top:2vh">
        <div class="q-big" style="font-size:1.4vw">多人协同下的“隐性破坏”防不胜防。代码写得越快，这种交互层面、边界状态的“改坏”就越多。</div>
      </div>
    </div>
    <!-- 右：AI 配图 -->
    <figure class="frame-img" style="height:60vh; align-self:center">
      <img src="https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=Abstract+representation+of+gears+moving+at+different+speeds+some+slightly+misaligned+representing+organizational+friction+clean+minimalist+light+theme&image_size=landscape_16_9" alt="组织速度与隐性破坏">
      <div class="frame-cap">
        <span class="pf">量变积累阶段的阵痛</span>
        <span class="idx">FIG. 02</span>
      </div>
    </figure>
  </div>
  <div class="foot">
    <div>效率瓶颈的转移</div>
    <div>— · —</div>
  </div>
</section>

<!-- Slide 9: 章节幕封 -->
<section class="slide hero dark">
  <div class="chrome">
    <div>第三幕 · 未来趋势</div>
    <div>Act III · 09 / 12</div>
  </div>
  <div class="frame" style="display:grid; gap:6vh; align-content:center; min-height:80vh">
    <div class="kicker">Act III</div>
    <h1 class="h-hero" style="font-size:8vw; font-family:var(--serif-zh); font-weight:700; letter-spacing:-0.02em">趋势：两个清晰的方向</h1>
    <p class="lead" style="max-width:55vw">
      基于一线的实践经验，我们看到了 AI Coding 正在发生的质变。
    </p>
  </div>
  <div class="foot">
    <div>场景泛化与协作模式变化</div>
    <div>— · —</div>
  </div>
</section>

<!-- Slide 10: 两列/并列 (趋势1) -->
<section class="slide light">
  <div class="chrome">
    <div>趋势 1 · 场景泛化</div>
    <div>Act III · 10 / 12</div>
  </div>
  <div class="frame" style="padding-top:6vh; display:flex; flex-direction:column">
    <div class="kicker">More Than Coding</div>
    <h2 class="h-xl" style="font-family:var(--serif-zh); font-weight:700; font-size:4vw; margin-bottom:8vh">AI Coding 正在成为基础设施</h2>
    
    <div class="split" style="flex:1; align-items:start; gap:8vw">
      <!-- 左侧 -->
      <div class="col" style="gap:3vh">
        <i class="ico ico-lg" data-lucide="arrow-up-down" style="opacity:0.5"></i>
        <h3 class="h3-zh" style="font-size:2.2vw">纵向：研发链条延伸</h3>
        <p class="body-zh">
          从需求分析、交互设计、编码研发，到质量保障、线上运维。整条链路上的角色都在从中受益，不再只是程序员的专属。
        </p>
      </div>
      <!-- 右侧 -->
      <div class="col" style="gap:3vh">
        <i class="ico ico-lg" data-lucide="expand" style="opacity:0.5"></i>
        <h3 class="h3-zh" style="font-size:2.2vw">横向：使用场景拓宽</h3>
        <p class="body-zh">
          技术调研、写设计文档、整理会议纪要，甚至管理本地知识库。AI 的价值远不止于写代码。这也是 SOLO 提供 Work 模式的原因。
        </p>
      </div>
    </div>
  </div>
  <div class="foot">
    <div>More Than Coding</div>
    <div>— · —</div>
  </div>
</section>

<!-- Slide 11: 左文右图 (趋势2) -->
<section class="slide dark">
  <div class="chrome">
    <div>趋势 2 · 协作模式</div>
    <div>Act III · 11 / 12</div>
  </div>
  <div class="frame grid-2-6-6" style="padding-top:4vh; gap:6vw">
    <!-- 左：文字 -->
    <div class="col" style="justify-content:center; gap:4vh">
      <div class="kicker">从执行者到决策者</div>
      <h2 class="h-xl" style="font-family:var(--serif-zh); font-weight:700; font-size:3.8vw; line-height:1.2">角色定位与<br>思维方式的升级</h2>
      <p class="body-zh">
        过去你是 <span class="hi">In the Loop</span>，每一行代码都经过你的手；现在你要学会 <span class="hi">On the Loop</span>，设定约束、委派任务、审查结果。
      </p>
      <div class="callout" style="margin-top:2vh">
        <div class="q-big" style="font-size:1.4vw">从命令式到声明式。你不再告诉 AI“怎么做”，而是声明“什么该是对的”，Agent 会持续保证它。</div>
      </div>
    </div>
    <!-- 右：AI 配图 -->
    <figure class="frame-img" style="height:60vh; align-self:center">
      <img src="https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=A+captain+overseeing+holographic+control+panels+in+a+futuristic+command+center+AI+agent+collaboration+dark+theme+cinematic+lighting&image_size=landscape_16_9" alt="On the Loop 监督">
      <div class="frame-cap">
        <span class="pf">在环外监督 (On the Loop)</span>
        <span class="idx">FIG. 03</span>
      </div>
    </figure>
  </div>
  <div class="foot">
    <div>协作模式的变化</div>
    <div>— · —</div>
  </div>
</section>

<!-- Slide 12: 悬念收束 / 结尾 -->
<section class="slide hero light">
  <div class="chrome">
    <div>终极形态</div>
    <div>End · 12 / 12</div>
  </div>
  <div class="frame" style="display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; padding:0 8vw; min-height:80vh">
    <div class="kicker" style="margin-bottom:4vh">未来已来</div>
    <h1 class="h-hero" style="font-size:7vw; font-family:var(--serif-zh); font-weight:700; letter-spacing:-0.02em; margin-bottom:4vh">自驾式的代码库</h1>
    <p class="lead" style="max-width:65vw; font-size:2vw; line-height:1.6; opacity:0.85">
      不是取代工程师，而是让每个工程师都能站在更高的抽象层次上思考和创造。
    </p>
    <div class="meta" style="margin-top:8vh; font-family:var(--serif-en); font-style:italic; font-size:1.5vw; opacity:0.6">
      Thank You.
    </div>
  </div>
  <div class="foot">
    <div>探索新范式</div>
    <div>— · —</div>
  </div>
</section>
"""

with open('/workspace/SOLO-0408-直播/ppt/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<!-- SLIDES_HERE -->', slides_html)

with open('/workspace/SOLO-0408-直播/ppt/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Slides generated and inserted.")
