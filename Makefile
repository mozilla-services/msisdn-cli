VENV := $(shell echo $${VIRTUAL_ENV-.venv})
INSTALL_STAMP=$(VENV)/.install.stamp

install: $(INSTALL_STAMP)

$(INSTALL_STAMP): setup.py
	virtualenv $(VENV)
	$(VENV)/bin/pip install -e ./
	touch $(INSTALL_STAMP)

clean:
	rm -fr $(VENV)
