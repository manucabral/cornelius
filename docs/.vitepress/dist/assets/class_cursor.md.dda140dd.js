import{_ as s,o as n,c as a,a as l}from"./app.728a3616.js";const d=JSON.parse('{"title":"class: Cursor","description":"","frontmatter":{"title":"class: Cursor"},"headers":[{"level":2,"title":"get()","slug":"get","link":"#get","children":[]},{"level":2,"title":"set()","slug":"set","link":"#set","children":[]},{"level":2,"title":"press()","slug":"press","link":"#press","children":[]},{"level":2,"title":"release()","slug":"release","link":"#release","children":[]},{"level":2,"title":"left_click()","slug":"left-click","link":"#left-click","children":[]},{"level":2,"title":"right_click()","slug":"right-click","link":"#right-click","children":[]},{"level":2,"title":"is_pressed()","slug":"is-pressed","link":"#is-pressed","children":[]},{"level":2,"title":"Constants","slug":"constants","link":"#constants","children":[]}],"relativePath":"class/cursor.md"}'),e={name:"class/cursor.md"},p=l(`<h1 id="cursor" tabindex="-1">Cursor <a class="header-anchor" href="#cursor" aria-hidden="true">#</a></h1><p>In this section will you see <em>Cursor</em> class information.</p><p>Cursor class contains methods for controlling the mouse.</p><h2 id="get" tabindex="-1"><code>get()</code> <a class="header-anchor" href="#get" aria-hidden="true">#</a></h2><p>Gets the current cursor position.</p><p><strong>Parameters:</strong></p><ul><li>x <em>(int)</em>: The vertical position in pixels.</li><li>y <em>(int)</em>: The horizontal position in pixels.</li><li>point <em>(POINT)</em></li></ul><p><strong>Returns:</strong></p><ul><li><code>tuple</code> with the next items.</li></ul><p><strong>Example:</strong></p><div class="language-python line-numbers-mode"><button class="copy"></button><span class="lang">python</span><pre><code><span class="line"><span style="color:#89DDFF;">from</span><span style="color:#A6ACCD;"> cornelius </span><span style="color:#89DDFF;">import</span><span style="color:#A6ACCD;"> Cursor</span></span>
<span class="line"><span style="color:#89DDFF;">from</span><span style="color:#A6ACCD;"> time </span><span style="color:#89DDFF;">import</span><span style="color:#A6ACCD;"> time</span><span style="color:#89DDFF;">,</span><span style="color:#A6ACCD;"> sleep</span></span>
<span class="line"></span>
<span class="line"><span style="color:#A6ACCD;">mouse </span><span style="color:#89DDFF;">=</span><span style="color:#A6ACCD;"> </span><span style="color:#82AAFF;">Cursor</span><span style="color:#89DDFF;">()</span></span>
<span class="line"><span style="color:#A6ACCD;">positions </span><span style="color:#89DDFF;">=</span><span style="color:#A6ACCD;"> </span><span style="color:#89DDFF;">[]</span></span>
<span class="line"></span>
<span class="line"><span style="color:#A6ACCD;">velocity </span><span style="color:#89DDFF;">=</span><span style="color:#A6ACCD;"> </span><span style="color:#F78C6C;">0.1</span><span style="color:#A6ACCD;"> </span><span style="color:#676E95;"># in seconds</span></span>
<span class="line"><span style="color:#A6ACCD;">record_time </span><span style="color:#89DDFF;">=</span><span style="color:#A6ACCD;"> </span><span style="color:#F78C6C;">5</span><span style="color:#A6ACCD;"> </span><span style="color:#676E95;"># in seconds</span></span>
<span class="line"></span>
<span class="line"><span style="color:#A6ACCD;">start </span><span style="color:#89DDFF;">=</span><span style="color:#A6ACCD;"> </span><span style="color:#82AAFF;">time</span><span style="color:#89DDFF;">()</span></span>
<span class="line"><span style="color:#A6ACCD;">elapsed </span><span style="color:#89DDFF;">=</span><span style="color:#A6ACCD;"> </span><span style="color:#F78C6C;">0</span></span>
<span class="line"><span style="color:#82AAFF;">print</span><span style="color:#89DDFF;">(</span><span style="color:#89DDFF;">&quot;</span><span style="color:#C3E88D;">Recording...</span><span style="color:#89DDFF;">&quot;</span><span style="color:#89DDFF;">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF;">while</span><span style="color:#A6ACCD;"> elapsed </span><span style="color:#89DDFF;">&lt;</span><span style="color:#A6ACCD;"> record_time</span><span style="color:#89DDFF;">:</span></span>
<span class="line highlighted"><span style="color:#A6ACCD;">  position </span><span style="color:#89DDFF;">=</span><span style="color:#A6ACCD;"> mouse</span><span style="color:#89DDFF;">.</span><span style="color:#82AAFF;">get</span><span style="color:#89DDFF;">()</span></span>
<span class="line"><span style="color:#A6ACCD;">  position</span><span style="color:#89DDFF;">.</span><span style="color:#82AAFF;">append</span><span style="color:#89DDFF;">(</span><span style="color:#82AAFF;">positions</span><span style="color:#89DDFF;">)</span></span>
<span class="line"><span style="color:#A6ACCD;">  elapsed </span><span style="color:#89DDFF;">=</span><span style="color:#A6ACCD;"> </span><span style="color:#82AAFF;">time</span><span style="color:#89DDFF;">()</span><span style="color:#A6ACCD;"> </span><span style="color:#89DDFF;">-</span><span style="color:#A6ACCD;"> start</span></span>
<span class="line"><span style="color:#A6ACCD;">  </span><span style="color:#82AAFF;">sleep</span><span style="color:#89DDFF;">(</span><span style="color:#82AAFF;">velocity</span><span style="color:#89DDFF;">)</span></span>
<span class="line"><span style="color:#A6ACCD;">    </span></span>
<span class="line"><span style="color:#89DDFF;">for</span><span style="color:#A6ACCD;"> position </span><span style="color:#89DDFF;">in</span><span style="color:#A6ACCD;"> positions</span><span style="color:#89DDFF;">:</span></span>
<span class="line"><span style="color:#A6ACCD;">  x</span><span style="color:#89DDFF;">,</span><span style="color:#A6ACCD;"> y</span><span style="color:#89DDFF;">,</span><span style="color:#A6ACCD;"> _ </span><span style="color:#89DDFF;">=</span><span style="color:#A6ACCD;"> position </span><span style="color:#676E95;"># _ is the pointer, we don&#39;t need it :)</span></span>
<span class="line"><span style="color:#A6ACCD;">  mouse</span><span style="color:#89DDFF;">.</span><span style="color:#82AAFF;">set</span><span style="color:#89DDFF;">(</span><span style="color:#82AAFF;">x</span><span style="color:#89DDFF;">,</span><span style="color:#82AAFF;"> y</span><span style="color:#89DDFF;">)</span></span>
<span class="line"></span></code></pre><div class="line-numbers-wrapper"><span class="line-number">1</span><br><span class="line-number">2</span><br><span class="line-number">3</span><br><span class="line-number">4</span><br><span class="line-number">5</span><br><span class="line-number">6</span><br><span class="line-number">7</span><br><span class="line-number">8</span><br><span class="line-number">9</span><br><span class="line-number">10</span><br><span class="line-number">11</span><br><span class="line-number">12</span><br><span class="line-number">13</span><br><span class="line-number">14</span><br><span class="line-number">15</span><br><span class="line-number">16</span><br><span class="line-number">17</span><br><span class="line-number">18</span><br><span class="line-number">19</span><br><span class="line-number">20</span><br><span class="line-number">21</span><br><span class="line-number">22</span><br></div></div><h2 id="set" tabindex="-1"><code>set()</code> <a class="header-anchor" href="#set" aria-hidden="true">#</a></h2><p>Sets the cursor position in pixels.</p><p><strong>Parameters:</strong></p><ul><li>x <em>(int)</em>: The vertical position in pixels.</li><li>y <em>(int)</em>: The horizontal position in pixels.</li></ul><p><strong>Returns:</strong> -&gt; <code>None</code></p><p><strong>Example:</strong></p><div class="language-python line-numbers-mode"><button class="copy"></button><span class="lang">python</span><pre><code><span class="line"><span style="color:#89DDFF;">from</span><span style="color:#A6ACCD;"> cornelius </span><span style="color:#89DDFF;">import</span><span style="color:#A6ACCD;"> Cursor</span></span>
<span class="line"><span style="color:#89DDFF;">from</span><span style="color:#A6ACCD;"> time </span><span style="color:#89DDFF;">import</span><span style="color:#A6ACCD;"> sleep</span></span>
<span class="line"></span>
<span class="line"><span style="color:#A6ACCD;">cursor </span><span style="color:#89DDFF;">=</span><span style="color:#A6ACCD;"> </span><span style="color:#82AAFF;">Cursor</span><span style="color:#89DDFF;">()</span></span>
<span class="line highlighted"><span style="color:#A6ACCD;">cursor</span><span style="color:#89DDFF;">.</span><span style="color:#82AAFF;">set</span><span style="color:#89DDFF;">(</span><span style="color:#F78C6C;">300</span><span style="color:#89DDFF;">,</span><span style="color:#82AAFF;"> </span><span style="color:#F78C6C;">200</span><span style="color:#89DDFF;">)</span><span style="color:#A6ACCD;"> </span><span style="color:#676E95;"># Setting the cursor position</span></span>
<span class="line"><span style="color:#A6ACCD;">cursor</span><span style="color:#89DDFF;">.</span><span style="color:#82AAFF;">press</span><span style="color:#89DDFF;">(</span><span style="color:#F78C6C;">1</span><span style="color:#89DDFF;">)</span></span>
<span class="line"><span style="color:#82AAFF;">sleep</span><span style="color:#89DDFF;">(</span><span style="color:#F78C6C;">1</span><span style="color:#89DDFF;">)</span></span>
<span class="line"><span style="color:#A6ACCD;">cursor</span><span style="color:#89DDFF;">.</span><span style="color:#82AAFF;">release</span><span style="color:#89DDFF;">(</span><span style="color:#F78C6C;">1</span><span style="color:#89DDFF;">)</span></span>
<span class="line"></span></code></pre><div class="line-numbers-wrapper"><span class="line-number">1</span><br><span class="line-number">2</span><br><span class="line-number">3</span><br><span class="line-number">4</span><br><span class="line-number">5</span><br><span class="line-number">6</span><br><span class="line-number">7</span><br><span class="line-number">8</span><br></div></div><h2 id="press" tabindex="-1"><code>press()</code> <a class="header-anchor" href="#press" aria-hidden="true">#</a></h2><p>Press a mouse button.</p><p><strong>Parameters:</strong></p><ul><li>button <em>(int)</em>: The button <strong>id</strong> to press (1: left | 2: right).</li></ul><p><strong>Raises:</strong></p><ul><li>InvalidButtonException <em>(CorneliusException)</em>: If the button isn&#39;t valid.</li></ul><p><strong>Returns:</strong> -&gt; <code>None</code></p><p><strong>Example:</strong></p><div class="language-python line-numbers-mode"><button class="copy"></button><span class="lang">python</span><pre><code><span class="line"><span style="color:#89DDFF;">from</span><span style="color:#A6ACCD;"> cornelius </span><span style="color:#89DDFF;">import</span><span style="color:#A6ACCD;"> Cursor</span></span>
<span class="line"></span>
<span class="line"><span style="color:#A6ACCD;">cursor </span><span style="color:#89DDFF;">=</span><span style="color:#A6ACCD;"> </span><span style="color:#82AAFF;">Cursor</span><span style="color:#89DDFF;">()</span></span>
<span class="line highlighted"><span style="color:#A6ACCD;">cursor</span><span style="color:#89DDFF;">.</span><span style="color:#82AAFF;">press</span><span style="color:#89DDFF;">(</span><span style="color:#F78C6C;">2</span><span style="color:#89DDFF;">)</span><span style="color:#A6ACCD;"> </span><span style="color:#676E95;"># Pressing the right button.</span></span>
<span class="line"><span style="color:#A6ACCD;">cursor</span><span style="color:#89DDFF;">.</span><span style="color:#82AAFF;">release</span><span style="color:#89DDFF;">(</span><span style="color:#F78C6C;">1</span><span style="color:#89DDFF;">)</span></span>
<span class="line"></span></code></pre><div class="line-numbers-wrapper"><span class="line-number">1</span><br><span class="line-number">2</span><br><span class="line-number">3</span><br><span class="line-number">4</span><br><span class="line-number">5</span><br></div></div><h2 id="release" tabindex="-1"><code>release()</code> <a class="header-anchor" href="#release" aria-hidden="true">#</a></h2><p>Release a mouse button.</p><p><strong>Parameters:</strong></p><ul><li>button <em>(int)</em>: The button <strong>id</strong> to release (1: left | 2: right).</li></ul><p><strong>Raises:</strong></p><ul><li>InvalidButtonException <em>(CorneliusException)</em>: If the button isn&#39;t valid.</li></ul><p><strong>Returns:</strong> -&gt; <code>None</code></p><p><strong>Example:</strong></p><div class="language-python line-numbers-mode"><button class="copy"></button><span class="lang">python</span><pre><code><span class="line"><span style="color:#89DDFF;">from</span><span style="color:#A6ACCD;"> cornelius </span><span style="color:#89DDFF;">import</span><span style="color:#A6ACCD;"> Cursor</span></span>
<span class="line"></span>
<span class="line"><span style="color:#A6ACCD;">cursor </span><span style="color:#89DDFF;">=</span><span style="color:#A6ACCD;"> </span><span style="color:#82AAFF;">Cursor</span><span style="color:#89DDFF;">()</span></span>
<span class="line"><span style="color:#A6ACCD;">cursor</span><span style="color:#89DDFF;">.</span><span style="color:#82AAFF;">press</span><span style="color:#89DDFF;">(</span><span style="color:#F78C6C;">1</span><span style="color:#89DDFF;">)</span></span>
<span class="line highlighted"><span style="color:#A6ACCD;">cursor</span><span style="color:#89DDFF;">.</span><span style="color:#82AAFF;">release</span><span style="color:#89DDFF;">(</span><span style="color:#F78C6C;">2</span><span style="color:#89DDFF;">)</span><span style="color:#A6ACCD;"> </span><span style="color:#676E95;"># Release button</span></span>
<span class="line"></span></code></pre><div class="line-numbers-wrapper"><span class="line-number">1</span><br><span class="line-number">2</span><br><span class="line-number">3</span><br><span class="line-number">4</span><br><span class="line-number">5</span><br></div></div><h2 id="left-click" tabindex="-1"><code>left_click()</code> <a class="header-anchor" href="#left-click" aria-hidden="true">#</a></h2><p>Send a left click.</p><p><strong>Parameters:</strong></p><ul><li>delay <em>(float)</em>: Delay between clicks in seconds.</li></ul><p><strong>Returns:</strong> -&gt; <code>None</code></p><p><strong>Example:</strong></p><div class="danger custom-block"><p class="custom-block-title">Error \u{1F6A8}</p><p>No examples was founded.</p></div><h2 id="right-click" tabindex="-1"><code>right_click()</code> <a class="header-anchor" href="#right-click" aria-hidden="true">#</a></h2><p>Send a right click.</p><p><strong>Parameters:</strong></p><ul><li>delay <em>(float)</em>: Delay between clicks in seconds.</li></ul><p><strong>Returns:</strong> -&gt; <code>None</code></p><p><strong>Example:</strong></p><div class="danger custom-block"><p class="custom-block-title">Error \u{1F6A8}</p><p>No examples was founded.</p></div><h2 id="is-pressed" tabindex="-1"><code>is_pressed()</code> <a class="header-anchor" href="#is-pressed" aria-hidden="true">#</a></h2><p><strong>Parameters:</strong></p><ul><li>button <em>(int)</em>: Button <strong>id</strong> to check. (1: left | 2: right).</li></ul><p><strong>Raises:</strong></p><ul><li>InvalidButtonException <em>(CorneliusException)</em>: If the button isn&#39;t valid.</li></ul><p><strong>Returns:</strong> -&gt; <code>boolean</code>: <em>True</em> if pressed, <em>False</em> otherwise.</p><p><strong>Example:</strong></p><div class="danger custom-block"><p class="custom-block-title">Error \u{1F6A8}</p><p>No examples was founded.</p></div><h2 id="constants" tabindex="-1">Constants <a class="header-anchor" href="#constants" aria-hidden="true">#</a></h2><ul><li>class <em>cornelius.Cursor.<strong>LEFT_BUTTON</strong></em></li><li>class <em>cornelius.Cursor.<strong>RIGHT_BUTTON</strong></em></li></ul>`,60),o=[p];function r(t,c,i,D,F,y){return n(),a("div",null,o)}const A=s(e,[["render",r]]);export{d as __pageData,A as default};