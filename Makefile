BUILD=python jinja_build/jinja_build.py

ALL_INC_DIRS=main/,main/css/,main/js/,main/job_exp/,main/oss_exp/,main/templates/

START_SRC=main/index.html

OUTPUT=output/index.html

$(OUTPUT): $(START_SRC)
	export USE_PHONE=Y
	mkdir -p output/
	$(BUILD) $(START_SRC) . $(ALL_INC_DIRS) > $(OUTPUT)

nophone: $(START_SRC)
	mkdir -p output/
	$(BUILD) $(START_SRC) . $(ALL_INC_DIRS) > $(OUTPUT)


test: $(OUTPUT)
	./validate/html5check.py --encoding=utf-8 output/index.html

.PHONY: clean

clean:
	@echo Cleaning the build environment
	@rm -f output/*

