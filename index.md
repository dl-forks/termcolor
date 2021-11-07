# termcolor

## Code cheatsheet

<table>
  <tbody>
    <tr>
      <td>reset</td>
      <td><code class="language-plaintext highlighter-rouge">\033[0m</code></td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th style="text-align: left">color</th>
      <th style="text-align: left">oct</th>
      <!--<th style="text-align: left">bash</th>-->
      <th style="text-align: center">xterm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left">reset</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">\033[0m</code></td>
      <!--<td style="text-align: left"><code class="language-plaintext highlighter-rouge">\e[0m</code></td>-->
      <td style="text-align: center">-</td>
    </tr>
    <tr>
      <td style="text-align: left">black</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">\033[0;30m</code></td>
      <!--<td style="text-align: left"><code class="language-plaintext highlighter-rouge">\e[30m</code></td>-->
      <td style="text-align: center; background-color: rgb(0, 0, 0); color: white">0, 0, 0</td>
    </tr>
    <tr>
      <td style="text-align: left">red</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">\033[0;31m</code></td>
      <!--<td style="text-align: left"><code class="language-plaintext highlighter-rouge">\e[31m</code></td>-->
      <td style="text-align: center; background-color: rgb(205, 0, 0); color: black">205, 0, 0</td>
    </tr>
    <tr>
      <td style="text-align: left">green</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">\033[0;32m</code></td>
      <td style="text-align: center; background-color: rgb(0, 205, 0); color: black">0, 205, 0</td>
    </tr>
    <tr>
      <td style="text-align: left">yellow</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">\033[0;33m</code></td>
      <td style="text-align: center; background-color: rgb(205, 205, 0); color: black">205, 205, 0</td>
    </tr>
    <tr>
      <td style="text-align: left">blue</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">\033[0;34m</code></td>
      <td style="text-align: center; background-color: rgb(0, 0, 238); color: black">0, 0, 238</td>
    </tr>
    <tr>
      <td style="text-align: left">magneta</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">\033[0;35m</code></td>
      <td style="text-align: center; background-color: rgb(205, 0, 205); color: black">205, 0, 205</td>
    </tr>
    <tr>
      <td style="text-align: left">cyan</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">\033[0;36m</code></td>
      <td style="text-align: center; background-color: rgb(0, 205, 205); color: black">0, 205, 205</td>
    </tr>
    <tr>
      <td style="text-align: left">white</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">\033[0;37m</code></td>
      <td style="text-align: center; background-color: rgb(229, 229, 229); color: black">229, 229, 229</td>
    </tr>
    <tr>
      <td style="text-align: left">gray</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">\033[0;90m</code></td>
      <td style="text-align: center; background-color: rgb(127, 127, 127); color: black">127, 127, 127</td>
    </tr>
    <tr>
      <td style="text-align: left">bright red</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">\033[0;91m</code></td>
      <td style="text-align: center; background-color: rgb(255, 0 ,0); color: black">255, 0 ,0</td>
    </tr>
    <tr>
      <td style="text-align: left">bright green</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">\033[0;92m</code></td>
      <td style="text-align: center; background-color: rgb(0, 255, 0); color: black">0, 255, 0</td>
    </tr>
    <tr>
      <td style="text-align: left">bright yellow</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">\033[0;93m</code></td>
      <td style="text-align: center; background-color: rgb(255, 255, 0); color: black">255, 255, 0</td>
    </tr>
    <tr>
      <td style="text-align: left">bright blue</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">\033[0;94m</code></td>
      <td style="text-align: center; background-color: rgb(92, 92, 255); color: black">92, 92, 255</td>
    </tr>
    <tr>
      <td style="text-align: left">bright magneta</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">\033[0;95m</code></td>
      <td style="text-align: center; background-color: rgb(255, 0, 255); color: black">255, 0, 255</td>
    </tr>
    <tr>
      <td style="text-align: left">bright cyan</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">\033[0;96m</code></td>
      <td style="text-align: center; background-color: rgb(0, 255, 255); color: black">0, 255, 255</td>
    </tr>
    <tr>
      <td style="text-align: left">bright white</td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">\033[0;97m</code></td>
      <td style="text-align: center; background-color: rgb(255, 255, 255); color: black">255, 255, 255</td>
    </tr>
  </tbody>
</table>
