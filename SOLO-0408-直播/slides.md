---
theme: seriph
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## SOLO 0418 直播 — 正文
  独立版发布与前线实践分享
drawings:
  persist: false
transition: slide-up
title: SOLO 0418 直播
---

# SOLO 0418 直播

独立版发布与前线实践分享

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    开始演讲 <carbon:arrow-right class="inline"/>
  </span>
</div>

---
transition: fade-out
---

# 开场

## 我的闭关历程

回顾过去的几年，每年的 11 月 15 日对我都有特殊意义：

- **2022 年 11 月 15 日**：加入字节跳动
- **2023 年 11 月 15 日**：闭关做出了 MarsCode Cloud IDE
- **2024 年 11 月 15 日**：闭关做出了 TRAE IDE
- **2025 年底**：最终还是闭关了，产出了今天的主角——**SOLO 独立版**

<br>

> **对 AI 的定义演进：**
> 从 "人人都配备的高潜实习生" 
> ➡️ 到 **"每个人专属的高级个人助理"**

---
transition: slide-up
---

## 认知升级与迭代

行业日新月异，认知在飞速跃迁：

- **2月份：** 认为 AI Coding 是野花，Tab Tab 才是过日子。Agent 时代还很远。
- **年中：** 提出 AI Coding 正在转向以 Agent 为中心的研发范式。IDE 能力被逐渐原子化，TRAE 融合了 IDE 与 SOLO 模式。
- **12月份：** 用 Agent 做长时间异步并行成为共识。
  - *案例：* 社区 Expert 徐飞，全年用 Agent 写 30万行代码，仅 Tab Tab 12次。
- **年底结论：** 原预期两年的“AI辅助”阶段被极速跨越，**AI自主编程时代已经到来**！

---
layout: center
class: text-center
---

## SOLO 独立版发布

正因为认知迭代太快，我们一直在奔跑。

2026 年初再次闭关，我们将 SOLO 从 IDE 中独立出来，成为真正独立的产品形态。

同时提供 **PC 和 Web** 两个版本。

---
layout: section
---

# 实践

## SOLO Powers SOLO：在前线看到了什么

<div class="flex justify-center mt-8">
  <img src="https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=An%20engineer%20collaborating%20with%20an%20AI%20assistant.%20Minimal%20hand-drawn%20illustration%2C%20off-white%20paper%20background%2C%20dark%20gray%20sketch%20lines%2C%20muted%20umbrella%20yellow%20as%20the%20only%20accent%20color%2C%20lots%20of%20negative%20space%2C%20Notion-like%20doodle%20aesthetic%2C%20faceless%20round-headed%20human%20figure%2C%20clean%20editorial%20composition%2C%20conceptual%20rather%20than%20literal%2C%20simple%20background%2C%20no%20realism%2C%20no%203D%2C%20no%20painterly%20texture%2C%20no%20high%20saturation%2C%20no%20complex%20scene%2C%20no%20photographic%20detail.%20Add%20one%20short%20Chinese%20quote%20%22%E4%BA%BA%E6%9C%BA%E5%8D%8F%E5%90%8C%22%20in%20a%20natural%20handwritten%20style%20near%20the%20bottom.%20The%20overall%20mood%20is%20restrained%2C%20lucid%2C%20slightly%20ironic%2C%20and%20emotionally%20calm.&image_size=landscape_16_9" class="w-160 rounded-xl shadow-lg border border-gray-200" />
</div>

---
transition: slide-up
---

## 吃自己的狗粮

我们在开发 SOLO 独立版的过程中，把自己作为最佳实践：

- **100 万行代码** 的总产出
- **9000 个 commit**
- **AI 的代码贡献率达到了惊人的 93%**

我们自己就是第一批深度用户，这类深度使用 Agent 的用户不在少数，这是一个非常明显的趋势变化。

---

## 实践中的 Good (令人兴奋的变化)

- **团队认知在跃迁：** 迈向 AI 自主编程阶段（AI为主力，人做决策和监督）。测试等维护成本大幅下降。
- **知识显性化的探索：** 从个人隐性知识 ➡️ 团队知识 ➡️ AI 能读懂的 Skill 文件。
  - 新人上手和问题排查经验转变为可复用的 Skill。

<br>

<div class="p-4 bg-gray-50 dark:bg-gray-800 rounded-lg shadow-sm">
  <p class="text-xl italic text-center">
    "我们今天的 93%，可能半年后就是你们的常态。"
  </p>
</div>

---

## 实践中的 Bad (真实的挑战)

坦白说，我们也遇到了不少真实的问题：

- **个人速度 ≠ 组织速度：**
  - AI 写代码快了一个数量级，但上下游沟通协调成本上升。
  - 产出变多，对项目的掌控感反而下降。
- **多人协同下的"隐性破坏"：**
  - 细微的交互、边界状态被改坏，难以被自动化测试覆盖。
  - 代码写得越快，这类隐性问题越多。

> 我们仍处于量变积累阶段，还未突破质变，重塑整个团队的研发流程还需要时间。

---
layout: section
---

# 趋势

基于实践，我们看到两个方向

---

## 趋势 1：场景泛化 — More Than Coding

AI Coding 正在从"产品能力"变成"基础设施能力"。

- **纵向延伸：** 贯穿研发全链条（需求分析、设计、编码、测试、部署、运维）。不再只是程序员用，整条链路都在受益。
- **横向拓宽：** 场景拓展到技术调研、写设计文档、整理会议纪要、知识库等。

<br>

**应对方案：** 
SOLO 独立版提供 **Code 模式** (面向编程) 与 **Work 模式** (面向更泛化的工作场景)。

---

## 趋势 2：协作模式变化 — 从执行者到决策者

- **角色定位升级：** 从 In the Loop ➡️ On the Loop（在环外监督）。
  - 设定约束、委派任务、审查结果。
  - 全天候、跨设备监督（PC + Web 端联动）。
- **认知与思维转换：** 从命令式（怎么做） ➡️ 声明式（什么是对的）。
  - **终极形态：自驾式的代码库。**
  - 声明期望状态（依赖最新、覆盖率达标、漏洞修复），Agent 持续保证。

---
layout: center
class: text-center
---

# 结语

拥抱新范式：不是取代工程师，而是让每个工程师都能站在更高的抽象层次上思考和创造。

接下来，由技术同事分享我们是如何用 SOLO 开发 SOLO 的真实工程实践和踩坑经验。

## 感谢聆听！
