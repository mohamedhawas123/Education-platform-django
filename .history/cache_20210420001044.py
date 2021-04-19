# class CourseListView(TemplateResponseMixin, View):
#     model = Course
#     template_name = 'courses/course/list.html'
#     def get(self, request, subject=None):
#         subjects = cache.get('all_subjects')
#         if not subjects:
#             subjects = Subject.objects.annotate(
#                            total_courses=Count('courses'))
#             cache.set('all_subjects', subjects)
#         all_courses = Course.objects.annotate(
#                            total_modules=Count('modules'))
#         if subject:
#             subject = get_object_or_404(Subject, slug=subject)
#             key = f'subject_{subject.id}_courses'
#             courses = cache.get(key)
#             if not courses:
#                 courses = all_courses.filter(subject=subject)
#                 cache.set(key, courses)
#         else:
#             courses = cache.get('all_courses')
#             if not courses:
#                 courses = all_courses
#                 cache.set('all_courses', courses)
#         return self.render_to_response({'subjects': subjects,
#                                         'subject': subject,
#                                         'courses': courses})