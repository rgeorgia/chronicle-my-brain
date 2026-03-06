.PHONY: gh-pages

gh-pages:
	@sphinx-build ./docs ./docs/gh-pages

ronverbs:
	@sphinx-build ./docs ./docs/ronverbs.org

prod-pages:
	doas rm -rf /var/vroot/
	doas /home/rgeorgia/.local/share/vcmb/bin/sphinx-build ./docs /var/www/htdocs/chronicle-my-brain
