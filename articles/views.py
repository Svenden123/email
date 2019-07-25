from django.shortcuts import render, redirect

from articles.models import Article, Profile


def show_articles(request):
    cur_user = request.user
    profile = Profile.objects.filter(user=cur_user).first()
    if profile and not (cur_user.is_authenticated and profile.subscription):
        context = Article.objects.all().filter(is_paid=False)
    else:
        context = Article.objects.all()

    return render(
        request,
        'articles.html', {'context': context}
    )


def show_article(request, id):
    cur_user = request.user
    profile = Profile.objects.filter(user=cur_user).first()
    article = Article.objects.get(pk=id)
    if article.is_paid and profile and not (cur_user.is_authenticated and profile.subscription):
        return redirect('/articles/')

    return render(
        request,
        'article.html', {'context': article}
    )
