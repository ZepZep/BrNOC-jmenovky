# BrNOC-jmenovky

#### Proces pro vytváření jmenovek
1. .csv soubor z databáze, sloupečky: jmeno; funkce
2. upravit skript `genTex.py`
  * nazvy funkcí
  * cesty k obrazkům
3. `python genTex.py [cesta k .csv]`
  * to vytvoří lidi.tex
  * překopírovat (a přejmenovat) `lidi.tex` do složky `tex`
4. uprvit 31. řádek souboru `jmenovky.tex`
5. `pdflatex jmenovky.tex`
  * výstup jmenovky.pdf
