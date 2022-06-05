import factory
from main_habit.models import *

from faker import Faker

faker = Faker()


class HabitSetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = HabitSet

    habit_topic = factory.LazyAttribute(lambda _: faker.name())


class HabitsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Habits

    name = factory.LazyAttribute(lambda _: faker.name())
    describe = factory.LazyAttribute(lambda _: faker.pystr(max_chars=126))
    habit_set = factory.SubFactory(HabitSetFactory)


# class ProfileFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Profile
#
#     user = User(email="t@m.ru", username="user", password="1234")
#
#     @factory.post_generation
#     def achieves(self, create, extracted):
#         if not create:
#             return
#
#         if extracted:
#             for achieve in extracted:
#                 self.achieves.add(achieve)
#
#     @factory.post_generation
#     def habit_sets(self, create, extracted):
#         if not create:
#             return
#
#         if extracted:
#             for habit_set in extracted:
#                 self.habit_sets.add(habit_set)
#
#     avatar = "static/main_habit/images/ava.jpg"
#
#
# class StatisticsFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Statistics
#
#     time = factory.LazyAttribute(lambda _: faker.date_time())
#     is_done = factory.LazyAttribute(lambda _: faker.boolean())
#     habit = factory.SubFactory(HabitsFactory)
#     profile = factory.SubFactory(ProfileFactory)
