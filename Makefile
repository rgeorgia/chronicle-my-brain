.PHONY: gh-pages

gh-pages:
	@sphinx-build ./docs ./docs/gh-pages

prod-pages:
	doas rm -rf /var/www/htdocs/chronicle-my-brain
	doas /home/rgeorgia/.local/share/myvenv/cmb/bin/sphinx-build ./docs /var/www/htdocs/chronicle-my-brain

