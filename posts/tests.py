from django.test import TestCase
from django.utils import timezone
from users.models import User
from .models import Post


class PostModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@test.com",
            fullname="테스터",
            phone="010-1111-1111",
            password="1234",
        )
        self.post = Post.objects.create(
            title="test post title",
            body="test post body",
            author=self.user,
            status=Post.StatusChoices.DRAFT,
            publish=timezone.now(),
        )

    def test_save_method(self):
        expected_result = "test-post-title"
        self.assertEqual(self.post.slug, expected_result)

    def tearDown(self):
        self.post.delete()
        self.user.delete()
