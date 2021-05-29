# from rest_framework.views import APIView
#
#
# class LikeView(APIView):
#     def get(self, request, *args, **kwargs):
#         post = get_object_or_404(Photo, id=kwargs.get('pk'))
#         if post.likes.filter(id=request.user.id).exists():
#             post.likes.remove(request.user)
#         else:
#             post.likes.add(request.user)
#         return HttpResponse(post.likes.count())
#
#
# class LikeCommentView(APIView):
#     def get(self, request, *args, **kwargs):
#         post = get_object_or_404(Comment, id=kwargs.get('pk'))
#         if post.likes.filter(id=request.user.id).exists():
#             post.likes.remove(request.user)
#         else:
#             post.likes.add(request.user)
#         return HttpResponse(post.likes.count())
