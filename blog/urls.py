from django.urls import path, re_path
from blog import views

app_name = 'blog'

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("drafts/", views.DraftListView.as_view(), name="post_draft_list"),
    #path("post/create/", views.PostCreateView.as_view(), name="post_create"),
    path("post/create/", views.create_post, name="post_create"),
    re_path(r"^post/(?P<pk>\d+)/$", views.PostDetailView.as_view(), name="post_detail"),
    re_path(
        r"^post/(?P<pk>\d+)/update/$",
        views.PostUpdateView.as_view(),
        name="post_edit",
    ),     
    re_path(
        r"^post/(?P<pk>\d+)/remove/$",
        views.PostRemoveView.as_view(),
        name="post_remove",
    ),     
    re_path(
        r"^post/(?P<pk>\d+)/publish/$",
        views.post_publish,
        name="post_publish",
    ),     
    re_path(
        r"^post/(?P<pk>\d+)/comment/$",
        views.add_comment_to_post,
        name="add_comment_to_post",
    ),     
    re_path(
        r"^comment/(?P<pk>\d+)/approve/$",
        views.comment_approve,
        name="comment_approve",
    ),        
    re_path(
        r"^comment/(?P<pk>\d+)/remove/$",
        views.comment_remove,
        name="comment_remove",
    ),    
]
