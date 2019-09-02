from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.views.generic import RedirectView


# def root(request):
#     return redirect('blog:post_list')

urlpatterns = [
    # url(r'^$', root, name='root'),
    url(r'^$', lambda r: redirect('post_list'), name='root'),
    # url(r'^$', RedirectView.as_view(pattern_name='blog:post_list')),

    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^shop/', include('shop.urls')),
    url(r'^dojo/', include('dojo.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  # media 파일 추가시 작성 해줘야 된다.


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]