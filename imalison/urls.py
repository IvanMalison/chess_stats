from django.conf.urls import patterns, url
import chess_stats.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
	'',
	url(
		r'^chess_stats/browse_moves/js/(?P<path>.*)$',
		'django.views.static.serve',
		{
			'document_root': 'chess_stats/templates/js/',
		}
	),
        url(
		r'^chess_stats/browse_moves/css/(?P<path>.*)$',
		'django.views.static.serve',
		{
			'document_root': 'chess_stats/templates/css/',
		}
	),
	url(
		r'^chess_stats/browse_moves/views/(?P<path>.*)$',
		'django.views.static.serve',
		{
			'document_root': 'chess_stats/templates/views/',
		}
	),
	url(r'chess_stats/browse_games/.*', chess_stats.views.UserGameBrowserView.as_view()),
	url(r'chess_stats/browse_moves/.*', chess_stats.views.UserMoveBrowserView.as_view()),
	url(r'chess_stats/get_stats/.*', chess_stats.views.get_game_stats)
)

