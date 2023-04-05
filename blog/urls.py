from django.urls import path, re_path
from blog import views

app_name = 'blog'

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("drafts/", views.DraftListView.as_view(), name="post_draft_list"),
    path("post/create/", views.PostCreateView.as_view(), name="post_create"),
    re_path(r"^post/(?P<pk>\w+)/$", views.AboutView.as_view(), name="post_detail"),
    re_path(
        r"^post/(?P<pk>\w+)/update/$",
        views.PostUpdateView.as_view(),
        name="post_update",
    ),     
    re_path(
        r"^post/(?P<pk>\w+)/delete/$",
        views.PostDeleteView.as_view(),
        name="post_delete",
    ),     
    re_path(
        r"^post/(?P<pk>\w+)/publish/$",
        views.post_publish,
        name="post_publish",
    ),     
    re_path(
        r"^post/(?P<pk>\w+)/comment/$",
        views.add_comment_to_post,
        name="add_comment_to_post",
    ),     
    re_path(
        r"^comment/(?P<pk>\w+)/approve/$",
        views.comment_approve,
        name="comment_approve",
    ),        
    re_path(
        r"^comment/(?P<pk>\w+)/remove/$",
        views.comment_remove,
        name="comment_remove",
    ),    
]
