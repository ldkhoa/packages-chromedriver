all: tarball

tarball:
	spectool -g chromedriver.spec

clean:
	git clean -ffd

.PHONY: all tarball clean
