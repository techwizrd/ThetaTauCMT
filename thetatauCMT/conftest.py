import pytest
from pytest_factoryboy import register
from django.core.management import call_command
from django.contrib.sites.models import Site
from ballots.tests.factories import BallotFactory, BallotCompleteFactory
from chapters.tests.factories import ChapterFactory, ChapterCurriculaFactory
from events.tests.factories import EventFactory
from finances.tests.factories import TransactionFactory
from regions.tests.factories import RegionFactory
from scores.tests.factories import ScoreChapterFactory
from submissions.tests.factories import SubmissionFactory
from tasks.tests.factories import TaskChapterFactory
from users.tests.factories import (
    UserFactory,
    UserAlterFactory,
    UserOrgParticipateFactory,
    UserSemesterGPAFactory,
    UserSemesterServiceHoursFactory,
    UserRoleChangeFactory,
    UserStatusChangeFactory,
)


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata", "scoretypes.json")
        call_command("loaddata", "tasks.json")
        current_site = Site.objects.get_current()
        current_site.socialapp_set.create(
            provider="google",
            name="google",
            client_id="1234567890",
            secret="0987654321",
        )


@pytest.fixture
def test_password():
    return "strong-test-pass"


@pytest.fixture
def auto_login_user(db, client, user_factory, test_password):
    def make_auto_login(user=None, make_officer=False):
        if user is None:
            user = user_factory.create(
                password=test_password, make_officer=make_officer
            )
        client.login(username=user.username, password=test_password)
        return client, user

    return make_auto_login


@pytest.fixture(params=["chrome", "firefox"], scope="session")
def driver_get(request):
    from selenium import webdriver

    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", web_driver)
    yield
    web_driver.close()


register(RegionFactory)
register(ChapterFactory)
register(ChapterCurriculaFactory)
register(EventFactory)
register(BallotFactory)
register(BallotCompleteFactory)
register(TransactionFactory)
register(ScoreChapterFactory)
register(SubmissionFactory)
register(TaskChapterFactory)
register(UserFactory)
register(UserAlterFactory)
register(UserOrgParticipateFactory)
register(UserSemesterGPAFactory)
register(UserSemesterServiceHoursFactory)
register(UserRoleChangeFactory)
register(UserStatusChangeFactory)
