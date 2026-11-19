# =====================================================================
#  "Mesa de control" de la tesis. Ejecutar desde la raíz del repo.
#  Escribe `make` o `make ayuda` para ver los comandos.
# =====================================================================
TESIS   := tesis
SALIDA  := salida
BUILD   := $(SALIDA)/build
LATEXMK := cd $(TESIS) && latexmk -r latexmkrc

.PHONY: ayuda pdf vigilar revisar contar figuras contexto convertir diff limpiar

ayuda:
	@echo "Comandos disponibles:"
	@echo "  make pdf        Compila la tesis -> salida/tesis.pdf"
	@echo "  make vigilar    Recompila automáticamente al guardar"
	@echo "  make revisar    Revisa LaTeX (chktex), marcas pendientes, citas y extensión (normativa)"
	@echo "  make contar     Cuenta palabras por capítulo (texcount)"
	@echo "  make figuras    Regenera figuras y tablas desde 04_analisis/scripts"
	@echo "  make contexto   Junta todo el contexto en salida/contexto_completo.md (para otra IA / NotebookLM)"
	@echo "  make convertir ARCHIVO=ruta.docx   Convierte Word/ODT/HTML a Markdown (copia al lado)"
	@echo "  make diff DESDE=v0.1               PDF con cambios marcados respecto a una versión (latexdiff)"
	@echo "  make limpiar    Borra archivos auxiliares"

pdf:
	@mkdir -p $(BUILD)
	$(LATEXMK) -pdf main.tex
	@cp $(BUILD)/main.pdf $(SALIDA)/tesis.pdf
	@echo "==> PDF listo: $(SALIDA)/tesis.pdf"

vigilar:
	@mkdir -p $(BUILD)
	$(LATEXMK) -pdf -pvc main.tex

revisar:
	@echo "== chktex (advertencias de estilo LaTeX) =="
	-@cd $(TESIS) && chktex -q -n1 -n8 -n12 -n13 -n24 -n36 -n44 main.tex  # 12 y 13: falsos positivos con siglas (IBC., DQO.)
	@echo ""
	@echo "== Marcas PENDIENTE / REVISAR en la tesis =="
	-@grep -rn --include=*.tex -E '\\(pendiente|revisar)\{' $(TESIS)/capitulos $(TESIS)/preliminares $(TESIS)/anexos | grep -v anexo_guia_plantilla || echo "Sin marcas pendientes."
	@echo ""
	@echo "== Citas que no están en referencias.bib =="
	-@python3 herramientas/verificar_citas.py
	@echo ""
	@echo "== Extensión según normativa ICV-611 =="
	-@python3 herramientas/verificar_extension.py

contar:
	@cd $(TESIS) && texcount -inc -total -sum -q main.tex | tail -n +1

figuras:
	@for s in 04_analisis/scripts/*.py; do echo "-> $$s"; python3 $$s || exit 1; done

contexto:
	@python3 herramientas/empaquetar_contexto.py

convertir:
	@test -n "$(ARCHIVO)" || (echo "Uso: make convertir ARCHIVO=ruta/al/archivo.docx" && exit 1)
	@bash herramientas/convertir.sh "$(ARCHIVO)"

diff:
	@test -n "$(DESDE)" || (echo "Uso: make diff DESDE=<etiqueta o commit git>" && exit 1)
	@bash herramientas/diff_versiones.sh "$(DESDE)"

limpiar:
	-$(LATEXMK) -C main.tex
	rm -rf $(BUILD)
