.PHONY: gh-pages

gh-pages:
	@sphinx-build ./docs ./docs/gh-pages

prod-pages:
	doas rm -rf /var/vroot/
	doas /home/rgeorgia/.local/share/myenv/cmb/bin/sphinx-build ./docs /var/vroot/

