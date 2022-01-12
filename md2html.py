#!/usr/bin/python3
# -*- coding: utf-8 -*-
# install markdown2 via: pip3 install markdown2
import markdown2

html_head = """
<!-- Hongzhuo Liang -->
<h1>Hongzhuo Liang</h1>
<hr>

<img src="img/liang.jpg" width="225" alt="Hongzhuo Liang" style="margin-left:25px;float:right; border-style:solid; border-width:1px; border-color:#000;">

<table>
    <tr>
    <td align="right" valign="top"><b>address:</b></td>
    <td>&nbsp; University of Hamburg<br />
        &nbsp; Faculty of Mathematics, Informatics and Natural Science<br />
        &nbsp; Department Informatics, Group TAMS<br />
        &nbsp; Vogt-K&ouml;lln-Str. 30<br />
        &nbsp; D-22527 Hamburg
    </td>
    </tr>
    <tr><td>&nbsp;</td><td>&nbsp;</td></tr>
    <tr>
    <td align="right"><b>position:</b></td>
    <td>&nbsp; PhD student</td>
    </tr>
    <tr>
    <td align="right"><b>room:</b></td>
    <td>&nbsp; F-331</td>
    </tr>
    <tr>
    <td align="right"><b>phone:</b></td>
    <td>&nbsp; +49 (0) 40 42883-2440</td>
    </tr>
    <tr>
    <td align="right"><b>fax:</b></td>
    <td>&nbsp; +49 (0) 40 42883-2397</td>
    </tr>
    <tr>
    <td align="right"><b>e-mail:</b></td>
    <td>&nbsp; <a href="mailto:hongzhuo.liang@uni-hamburg.de">hongzhuo.liang@uni-hamburg.de</a></td><td>
    </tr>
    <tr>
    <td align="right"><b>github:</b></td>
    <td>&nbsp; <a href="https://github.com/lianghongzhuo">https://github.com/lianghongzhuo</a></td><td>
    </tr>
</table>
"""

# python3 -m markdown2 publications.md > publications.html
html = markdown2.markdown_path("publications.md")
with open("index.inc", "w") as h:\
    h.write(html_head + html[62:])
print("run this code to update the tams website:")
print("scp index.inc liang@rzssh1.informatik.uni-hamburg.de:/informatik2/tams/public/www/htdocs/people/liang")
