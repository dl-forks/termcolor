# Color codes cheatsheet

Changing text/background color can be accomplished by inserting special byte sequences called
<i>ANSI escape sequences</i> (<a href="https://en.wikipedia.org/wiki/ANSI_escape_code">wiki</a>).

Sequences that control colors look like <code class="highlighter-rouge">ESC[30;47m</code>,
where <code class="highlighter-rouge">ESC</code> is ASCII escape character 
(octal: <code class="highlighter-rouge">\033</code>, 
hex: <code class="highlighter-rouge">\x1B</code>), and numbers beetween bracket and
<code class="highlighter-rouge">m</code> determine what color will be used.

Bash shell <a href="https://www.gnu.org/software/bash/manual/html_node/ANSI_002dC-Quoting.html">allows</a>
using <code class="highlighter-rouge">\e</code> instead of
<code class="highlighter-rouge">\033</code> (brings some readability).

## 4-bit mode

<table style="width: 100%">
  <thead>
    <tr>
      <th>name</th>
      <th>code</th>
      <th>description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left"><i>reset</i></td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">0</span>m</code>
      </td>
      <td style="text-align: left">
        Resets text color, background color and other attributes.
      </td>
    </tr>
    <tr>
      <td style="text-align: left">bold</td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">1</span>m</code>
      </td>
      <td style="text-align: left">
        Bold or increased intensity.
      </td>
    </tr>
    <tr>
      <td style="text-align: left">dim</td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">2</span>m</code>
      </td>
      <td style="text-align: left">
        Light or decreased intensity.
      </td>
    </tr>
    <tr>
      <td style="text-align: left">italic</td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">3</span>m</code>
      </td>
      <td style="text-align: left">
          Not widely supported.
      </td>
    </tr>
    <tr>
      <td style="text-align: left">underline</td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">4</span>m</code>
      </td>
      <td style="text-align: left"></td>
    </tr>
    <tr>
      <td style="text-align: left">invert</td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">7</span>m</code>
      </td>
      <td style="text-align: left">
          Swap foreground and background colors.
      </td>
    </tr>
    <tr><td colspan="3" class="smaller note" style="text-align: right;">Some of the obsolete/unpopular attributes are skipped.</td></tr>
</tbody>
</table>

<table>
<tbody>
    <tr>
      <th>color</th>
      <th>text</th>
      <th>bg</th>
      <th>xterm</th>
    </tr>
    <tr>
      <td style="text-align: left">black</td>
      <td>
        <code class="highlighter-rouge">\033[<span class="char-hl">30</span>m</code>
      </td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">40</span>m</code>
      </td>
      <td style="text-align: center; background-color: rgb(0, 0, 0); color: white">0, 0, 0</td>
    </tr>
    <tr>
      <td style="text-align: left">red</td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">31</span>m</code>
      </td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">41</span>m</code>
      </td>
      <td style="text-align: center; background-color: rgb(205, 0, 0); color: black">205, 0, 0</td>
    </tr>
    <tr>
      <td style="text-align: left">green</td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">42</span>m</code>
      </td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">40</span>m</code>
      </td>
      <td style="text-align: center; background-color: rgb(0, 205, 0); color: black">0, 205, 0</td>
    </tr>
    <tr>
      <td style="text-align: left">yellow</td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">33</span>m</code>
      </td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">43</span>m</code>
      </td>
      <td style="text-align: center; background-color: rgb(205, 205, 0); color: black">205, 205, 0</td>
    </tr>
    <tr>
      <td style="text-align: left">blue</td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">34</span>m</code>
      </td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">44</span>m</code>
      </td>
      <td style="text-align: center; background-color: rgb(0, 0, 238); color: black">0, 0, 238</td>
    </tr>
    <tr>
      <td style="text-align: left">magneta</td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">35</span>m</code>
      </td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">45</span>m</code>
      </td>
      <td style="text-align: center; background-color: rgb(205, 0, 205); color: black">205, 0, 205</td>
    </tr>
    <tr>
      <td style="text-align: left">cyan</td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">36</span>m</code>
      </td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">46</span>m</code>
      </td>
      <td style="text-align: center; background-color: rgb(0, 205, 205); color: black">0, 205, 205</td>
    </tr>
    <tr>
      <td style="text-align: left">white</td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">37</span>m</code>
      </td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">47</span>m</code>
      </td>
      <td style="text-align: center; background-color: rgb(229, 229, 229); color: black">229, 229, 229</td>
    </tr>
    <tr>
      <td style="text-align: left">gray</td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">90</span>m</code>
      </td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">100</span>m</code>
      </td>
      <td style="text-align: center; background-color: rgb(127, 127, 127); color: black">127, 127, 127</td>
    </tr>
    <tr>
      <td style="text-align: left">bright red</td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">91</span>m</code>
      </td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">101</span>m</code>
      </td>
      <td style="text-align: center; background-color: rgb(255, 0 ,0); color: black">255, 0 ,0</td>
    </tr>
    <tr>
      <td style="text-align: left">bright green</td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">92</span>m</code>
      </td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">102</span>m</code>
      </td>
      <td style="text-align: center; background-color: rgb(0, 255, 0); color: black">0, 255, 0</td>
    </tr>
    <tr>
      <td style="text-align: left">bright yellow</td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">93</span>m</code>
      </td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">103</span>m</code>
      </td>
      <td style="text-align: center; background-color: rgb(255, 255, 0); color: black">255, 255, 0</td>
    </tr>
    <tr>
      <td style="text-align: left">bright blue</td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">94</span>m</code>
      </td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">104</span>m</code>
      </td>
      <td style="text-align: center; background-color: rgb(92, 92, 255); color: black">92, 92, 255</td>
    </tr>
    <tr>
      <td style="text-align: left">bright magneta</td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">95</span>m</code>
      </td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">105</span>m</code>
      </td>
      <td style="text-align: center; background-color: rgb(255, 0, 255); color: black">255, 0, 255</td>
    </tr>
    <tr>
      <td style="text-align: left">bright cyan</td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">96</span>m</code>
      </td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">106</span>m</code>
      </td>
      <td style="text-align: center; background-color: rgb(0, 255, 255); color: black">0, 255, 255</td>
    </tr>
    <tr>
      <td style="text-align: left">bright white</td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">97</span>m</code>
      </td>
      <td>
          <code class="highlighter-rouge">\033[<span class="char-hl">107</span>m</code>
      </td>
      <td style="text-align: center; background-color: rgb(255, 255, 255); color: black">255, 255, 255</td>
    </tr>
  </tbody>
</table>

## 8-bit mode

Sequence <code class="highlighter-rouge">ESC[<span class="char-hl">38</span>;<span class="char-hl">5</span>;<span class="char-hl"><i>X</i></span>m</code>
sets text color to <i>X</i>, and <code class="highlighter-rouge">ESC[<span class="char-hl">48</span>;<span class="char-hl">5</span>;<span class="char-hl"><i>Y</i></span>m</code> 
sets background color to <i>Y</i> (when operating in 256-colors mode). Color codes are different:

<table class="smaller">
  <tr>
    <td colspan="8" style="text-align: center"><h3>Standard colors</h3></td>
    <td colspan="8" style="text-align: center"><h3>High-intensity colors</h3></td>
  </tr>
  <tr>
<td style="color:#ffffff;background:#000000;">0
</td>
<td style="color:#ffffff;background:#800000;">1
</td>
<td style="color:#ffffff;background:#008000;">2
</td>
<td style="color:#ffffff;background:#808000;">3
</td>
<td style="color:#ffffff;background:#000080;">4
</td>
<td style="color:#ffffff;background:#800080;">5
</td>
<td style="color:#ffffff;background:#008080;">6
</td>
<td style="color:#ffffff;background:#c0c0c0;">7
</td>
<td style="color:#000000;background:#808080;">8
</td>
<td style="color:#000000;background:#ff0000;">9
</td>
<td style="color:#000000;background:#00ff00;">10
</td>
<td style="color:#000000;background:#ffff00;">11
</td>
<td style="color:#000000;background:#0000ff;">12
</td>
<td style="color:#000000;background:#ff00ff;">13
</td>
<td style="color:#000000;background:#00ffff;">14
</td>
<td style="color:#000000;background:#ffffff;">15
</td>
</tr>
</table>

<table class="smaller">
  <tr>
    <td colspan="18" style="text-align: center"><h3>216 colors</h3></td>
  </tr>
  <tr>
  <td style="color:#ffffff;background:#000000;">16
  </td>
  <td style="color:#ffffff;background:#00005f;">17
  </td>
  <td style="color:#ffffff;background:#000087;">18
  </td>
  <td style="color:#ffffff;background:#0000af;">19
  </td>
  <td style="color:#ffffff;background:#0000d7;">20
  </td>
  <td style="color:#ffffff;background:#0000ff;">21
  </td>
  <td style="color:#ffffff;background:#005f00;">22
  </td>
  <td style="color:#ffffff;background:#005f5f;">23
  </td>
  <td style="color:#ffffff;background:#005f87;">24
  </td>
  <td style="color:#ffffff;background:#005faf;">25
  </td>
  <td style="color:#ffffff;background:#005fd7;">26
  </td>
  <td style="color:#ffffff;background:#005fff;">27
  </td>
  <td style="color:#ffffff;background:#008700;">28
  </td>
  <td style="color:#ffffff;background:#00875f;">29
  </td>
  <td style="color:#ffffff;background:#008787;">30
  </td>
  <td style="color:#ffffff;background:#0087af;">31
  </td>
  <td style="color:#ffffff;background:#0087d7;">32
  </td>
  <td style="color:#ffffff;background:#0087ff;">33
  </td>
  </tr>

  <tr>
  <td style="color:#ffffff;background:#5f0000;">52
  </td>
  <td style="color:#ffffff;background:#5f005f;">53
  </td>
  <td style="color:#ffffff;background:#5f0087;">54
  </td>
  <td style="color:#ffffff;background:#5f00af;">55
  </td>
  <td style="color:#ffffff;background:#5f00d7;">56
  </td>
  <td style="color:#ffffff;background:#5f00ff;">57
  </td>
  <td style="color:#ffffff;background:#5f5f00;">58
  </td>
  <td style="color:#ffffff;background:#5f5f5f;">59
  </td>
  <td style="color:#ffffff;background:#5f5f87;">60
  </td>
  <td style="color:#ffffff;background:#5f5faf;">61
  </td>
  <td style="color:#ffffff;background:#5f5fd7;">62
  </td>
  <td style="color:#ffffff;background:#5f5fff;">63
  </td>
  <td style="color:#ffffff;background:#5f8700;">64
  </td>
  <td style="color:#ffffff;background:#5f875f;">65
  </td>
  <td style="color:#ffffff;background:#5f8787;">66
  </td>
  <td style="color:#ffffff;background:#5f87af;">67
  </td>
  <td style="color:#ffffff;background:#5f87d7;">68
  </td>
  <td style="color:#ffffff;background:#5f87ff;">69
  </td>
  </tr>
  <tr>
  <td style="color:#ffffff;background:#870000;">88
  </td>
  <td style="color:#ffffff;background:#87005f;">89
  </td>
  <td style="color:#ffffff;background:#870087;">90
  </td>
  <td style="color:#ffffff;background:#8700af;">91
  </td>
  <td style="color:#ffffff;background:#8700d7;">92
  </td>
  <td style="color:#ffffff;background:#8700ff;">93
  </td>
  <td style="color:#ffffff;background:#875f00;">94
  </td>
  <td style="color:#ffffff;background:#875f5f;">95
  </td>
  <td style="color:#ffffff;background:#875f87;">96
  </td>
  <td style="color:#ffffff;background:#875faf;">97
  </td>
  <td style="color:#ffffff;background:#875fd7;">98
  </td>
  <td style="color:#ffffff;background:#875fff;">99
  </td>
  <td style="color:#ffffff;background:#878700;">100
  </td>
  <td style="color:#ffffff;background:#87875f;">101
  </td>
  <td style="color:#ffffff;background:#878787;">102
  </td>
  <td style="color:#ffffff;background:#8787af;">103
  </td>
  <td style="color:#ffffff;background:#8787d7;">104
  </td>
  <td style="color:#ffffff;background:#8787ff;">105
  </td>
  </tr>
  <tr>
  <td style="color:#ffffff;background:#af0000;">124
  </td>
  <td style="color:#ffffff;background:#af005f;">125
  </td>
  <td style="color:#ffffff;background:#af0087;">126
  </td>
  <td style="color:#ffffff;background:#af00af;">127
  </td>
  <td style="color:#ffffff;background:#af00d7;">128
  </td>
  <td style="color:#ffffff;background:#af00ff;">129
  </td>
  <td style="color:#ffffff;background:#af5f00;">130
  </td>
  <td style="color:#ffffff;background:#af5f5f;">131
  </td>
  <td style="color:#ffffff;background:#af5f87;">132
  </td>
  <td style="color:#ffffff;background:#af5faf;">133
  </td>
  <td style="color:#ffffff;background:#af5fd7;">134
  </td>
  <td style="color:#ffffff;background:#af5fff;">135
  </td>
  <td style="color:#ffffff;background:#af8700;">136
  </td>
  <td style="color:#ffffff;background:#af875f;">137
  </td>
  <td style="color:#ffffff;background:#af8787;">138
  </td>
  <td style="color:#ffffff;background:#af87af;">139
  </td>
  <td style="color:#ffffff;background:#af87d7;">140
  </td>
  <td style="color:#ffffff;background:#af87ff;">141
  </td>
  </tr>
  <tr>
  <td style="color:#ffffff;background:#d70000;">160
  </td>
  <td style="color:#ffffff;background:#d7005f;">161
  </td>
  <td style="color:#ffffff;background:#d70087;">162
  </td>
  <td style="color:#ffffff;background:#d700af;">163
  </td>
  <td style="color:#ffffff;background:#d700d7;">164
  </td>
  <td style="color:#ffffff;background:#d700ff;">165
  </td>
  <td style="color:#ffffff;background:#d75f00;">166
  </td>
  <td style="color:#ffffff;background:#d75f5f;">167
  </td>
  <td style="color:#ffffff;background:#d75f87;">168
  </td>
  <td style="color:#ffffff;background:#d75faf;">169
  </td>
  <td style="color:#ffffff;background:#d75fd7;">170
  </td>
  <td style="color:#ffffff;background:#d75fff;">171
  </td>
  <td style="color:#ffffff;background:#d78700;">172
  </td>
  <td style="color:#ffffff;background:#d7875f;">173
  </td>
  <td style="color:#ffffff;background:#d78787;">174
  </td>
  <td style="color:#ffffff;background:#d787af;">175
  </td>
  <td style="color:#ffffff;background:#d787d7;">176
  </td>
  <td style="color:#ffffff;background:#d787ff;">177
  </td>
  </tr>
  <tr>
  <td style="color:#ffffff;background:#ff0000;">196
  </td>
  <td style="color:#ffffff;background:#ff005f;">197
  </td>
  <td style="color:#ffffff;background:#ff0087;">198
  </td>
  <td style="color:#ffffff;background:#ff00af;">199
  </td>
  <td style="color:#ffffff;background:#ff00d7;">200
  </td>
  <td style="color:#ffffff;background:#ff00ff;">201
  </td>
  <td style="color:#ffffff;background:#ff5f00;">202
  </td>
  <td style="color:#ffffff;background:#ff5f5f;">203
  </td>
  <td style="color:#ffffff;background:#ff5f87;">204
  </td>
  <td style="color:#ffffff;background:#ff5faf;">205
  </td>
  <td style="color:#ffffff;background:#ff5fd7;">206
  </td>
  <td style="color:#ffffff;background:#ff5fff;">207
  </td>
  <td style="color:#ffffff;background:#ff8700;">208
  </td>
  <td style="color:#ffffff;background:#ff875f;">209
  </td>
  <td style="color:#ffffff;background:#ff8787;">210
  </td>
  <td style="color:#ffffff;background:#ff87af;">211
  </td>
  <td style="color:#ffffff;background:#ff87d7;">212
  </td>
  <td style="color:#ffffff;background:#ff87ff;">213
  </td>
  </tr>
  <tr>
  <td style="color:#000000;background:#00af00;">34
  </td>
  <td style="color:#000000;background:#00af5f;">35
  </td>
  <td style="color:#000000;background:#00af87;">36
  </td>
  <td style="color:#000000;background:#00afaf;">37
  </td>
  <td style="color:#000000;background:#00afd7;">38
  </td>
  <td style="color:#000000;background:#00afff;">39
  </td>
  <td style="color:#000000;background:#00d700;">40
  </td>
  <td style="color:#000000;background:#00d75f;">41
  </td>
  <td style="color:#000000;background:#00d787;">42
  </td>
  <td style="color:#000000;background:#00d7af;">43
  </td>
  <td style="color:#000000;background:#00d7d7;">44
  </td>
  <td style="color:#000000;background:#00d7ff;">45
  </td>
  <td style="color:#000000;background:#00ff00;">46
  </td>
  <td style="color:#000000;background:#00ff5f;">47
  </td>
  <td style="color:#000000;background:#00ff87;">48
  </td>
  <td style="color:#000000;background:#00ffaf;">49
  </td>
  <td style="color:#000000;background:#00ffd7;">50
  </td>
  <td style="color:#000000;background:#00ffff;">51
  </td></tr>
  <tr>
  <td style="color:#000000;background:#5faf00;">70
  </td>
  <td style="color:#000000;background:#5faf5f;">71
  </td>
  <td style="color:#000000;background:#5faf87;">72
  </td>
  <td style="color:#000000;background:#5fafaf;">73
  </td>
  <td style="color:#000000;background:#5fafd7;">74
  </td>
  <td style="color:#000000;background:#5fafff;">75
  </td>
  <td style="color:#000000;background:#5fd700;">76
  </td>
  <td style="color:#000000;background:#5fd75f;">77
  </td>
  <td style="color:#000000;background:#5fd787;">78
  </td>
  <td style="color:#000000;background:#5fd7af;">79
  </td>
  <td style="color:#000000;background:#5fd7d7;">80
  </td>
  <td style="color:#000000;background:#5fd7ff;">81
  </td>
  <td style="color:#000000;background:#5fff00;">82
  </td>
  <td style="color:#000000;background:#5fff5f;">83
  </td>
  <td style="color:#000000;background:#5fff87;">84
  </td>
  <td style="color:#000000;background:#5fffaf;">85
  </td>
  <td style="color:#000000;background:#5fffd7;">86
  </td>
  <td style="color:#000000;background:#5fffff;">87
  </td></tr>
  <tr>
  <td style="color:#000000;background:#87af00;">106
  </td>
  <td style="color:#000000;background:#87af5f;">107
  </td>
  <td style="color:#000000;background:#87af87;">108
  </td>
  <td style="color:#000000;background:#87afaf;">109
  </td>
  <td style="color:#000000;background:#87afd7;">110
  </td>
  <td style="color:#000000;background:#87afff;">111
  </td>
  <td style="color:#000000;background:#87d700;">112
  </td>
  <td style="color:#000000;background:#87d75f;">113
  </td>
  <td style="color:#000000;background:#87d787;">114
  </td>
  <td style="color:#000000;background:#87d7af;">115
  </td>
  <td style="color:#000000;background:#87d7d7;">116
  </td>
  <td style="color:#000000;background:#87d7ff;">117
  </td>
  <td style="color:#000000;background:#87ff00;">118
  </td>
  <td style="color:#000000;background:#87ff5f;">119
  </td>
  <td style="color:#000000;background:#87ff87;">120
  </td>
  <td style="color:#000000;background:#87ffaf;">121
  </td>
  <td style="color:#000000;background:#87ffd7;">122
  </td>
  <td style="color:#000000;background:#87ffff;">123
  </td></tr>
  <tr>
  <td style="color:#000000;background:#afaf00;">142
  </td>
  <td style="color:#000000;background:#afaf5f;">143
  </td>
  <td style="color:#000000;background:#afaf87;">144
  </td>
  <td style="color:#000000;background:#afafaf;">145
  </td>
  <td style="color:#000000;background:#afafd7;">146
  </td>
  <td style="color:#000000;background:#afafff;">147
  </td>
  <td style="color:#000000;background:#afd700;">148
  </td>
  <td style="color:#000000;background:#afd75f;">149
  </td>
  <td style="color:#000000;background:#afd787;">150
  </td>
  <td style="color:#000000;background:#afd7af;">151
  </td>
  <td style="color:#000000;background:#afd7d7;">152
  </td>
  <td style="color:#000000;background:#afd7ff;">153
  </td>
  <td style="color:#000000;background:#afff00;">154
  </td>
  <td style="color:#000000;background:#afff5f;">155
  </td>
  <td style="color:#000000;background:#afff87;">156
  </td>
  <td style="color:#000000;background:#afffaf;">157
  </td>
  <td style="color:#000000;background:#afffd7;">158
  </td>
  <td style="color:#000000;background:#afffff;">159
  </td></tr>
  <tr>
  <td style="color:#000000;background:#d7af00;">178
  </td>
  <td style="color:#000000;background:#d7af5f;">179
  </td>
  <td style="color:#000000;background:#d7af87;">180
  </td>
  <td style="color:#000000;background:#d7afaf;">181
  </td>
  <td style="color:#000000;background:#d7afd7;">182
  </td>
  <td style="color:#000000;background:#d7afff;">183
  </td>
  <td style="color:#000000;background:#d7d700;">184
  </td>
  <td style="color:#000000;background:#d7d75f;">185
  </td>
  <td style="color:#000000;background:#d7d787;">186
  </td>
  <td style="color:#000000;background:#d7d7af;">187
  </td>
  <td style="color:#000000;background:#d7d7d7;">188
  </td>
  <td style="color:#000000;background:#d7d7ff;">189
  </td>
  <td style="color:#000000;background:#d7ff00;">190
  </td>
  <td style="color:#000000;background:#d7ff5f;">191
  </td>
  <td style="color:#000000;background:#d7ff87;">192
  </td>
  <td style="color:#000000;background:#d7ffaf;">193
  </td>
  <td style="color:#000000;background:#d7ffd7;">194
  </td>
  <td style="color:#000000;background:#d7ffff;">195
  </td></tr>
  <tr>
  <td style="color:#000000;background:#ffaf00;">214
  </td>
  <td style="color:#000000;background:#ffaf5f;">215
  </td>
  <td style="color:#000000;background:#ffaf87;">216
  </td>
  <td style="color:#000000;background:#ffafaf;">217
  </td>
  <td style="color:#000000;background:#ffafd7;">218
  </td>
  <td style="color:#000000;background:#ffafff;">219
  </td>
  <td style="color:#000000;background:#ffd700;">220
  </td>
  <td style="color:#000000;background:#ffd75f;">221
  </td>
  <td style="color:#000000;background:#ffd787;">222
  </td>
  <td style="color:#000000;background:#ffd7af;">223
  </td>
  <td style="color:#000000;background:#ffd7d7;">224
  </td>
  <td style="color:#000000;background:#ffd7ff;">225
  </td>
  <td style="color:#000000;background:#ffff00;">226
  </td>
  <td style="color:#000000;background:#ffff5f;">227
  </td>
  <td style="color:#000000;background:#ffff87;">228
  </td>
  <td style="color:#000000;background:#ffffaf;">229
  </td>
  <td style="color:#000000;background:#ffffd7;">230
  </td>
  <td style="color:#000000;background:#ffffff;">231
  </td></tr>
</table>

<table class="smaller">
  <tr>
    <td colspan="16" style="text-align: center">
      <h3>Grayscale colors</h3>
    </td>
  </tr>
  <tr>
  <td style="color:#ffffff;background:#080808;">232
  </td>
  <td style="color:#ffffff;background:#121212;">233
  </td>
  <td style="color:#ffffff;background:#1c1c1c;">234
  </td>
  <td style="color:#ffffff;background:#262626;">235
  </td>
  <td style="color:#ffffff;background:#303030;">236
  </td>
  <td style="color:#ffffff;background:#3a3a3a;">237
  </td>
  <td style="color:#ffffff;background:#444444;">238
  </td>
  <td style="color:#ffffff;background:#4e4e4e;">239
  </td>
  <td style="color:#ffffff;background:#585858;">240
  </td>
  <td style="color:#ffffff;background:#626262;">241
  </td>
  <td style="color:#ffffff;background:#6c6c6c;">242
  </td>
  <td style="color:#ffffff;background:#767676;">243
  </td>
</tr>
<tr>
  <td style="color:#000000;background:#808080;">244
  </td>
  <td style="color:#000000;background:#8a8a8a;">245
  </td>
  <td style="color:#000000;background:#949494;">246
  </td>
  <td style="color:#000000;background:#9e9e9e;">247
  </td>
  <td style="color:#000000;background:#a8a8a8;">248
  </td>
  <td style="color:#000000;background:#b2b2b2;">249
  </td>
  <td style="color:#000000;background:#bcbcbc;">250
  </td>
  <td style="color:#000000;background:#c6c6c6;">251
  </td>
  <td style="color:#000000;background:#d0d0d0;">252
  </td>
  <td style="color:#000000;background:#dadada;">253
  </td>
  <td style="color:#000000;background:#e4e4e4;">254
  </td>
  <td style="color:#000000;background:#eeeeee;">255
  </td>
</tr>
</table>

<div class="footer">
</div>