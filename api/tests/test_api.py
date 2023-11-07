import requests

from approvaltests import verify_as_json, Options,  DiffReporter

API_BASE = f"http://localhost:8000"

class TestAPIRoot:

    def _verify(self, endpoint: str):
        response = requests.get(API_BASE + endpoint, allow_redirects=True, headers = {'Accept': 'application/json'}).json()

        verify_as_json(response, options=Options().with_reporter(DiffReporter()))

    def test_root(self):
        self._verify(f"/")

    # Specific tests like these should be aimed at spots where there have been bugs before, to prevent regression.
    def test_magic_missile(self):
        self._verify(f"/spells/magic-missile/")

    # Endpoint tests ensure that the basic structure and count of the objects does not change by accident. It's not a comprehensive test of all items.

    def test_armor(self):
        self._verify("/armor")

    def test_backgrounds(self):
        self._verify("/backgrounds")

    def test_classes(self):
        self._verify("/classes")

    def test_conditions(self):
        self._verify("/conditions")

    def test_documents(self):
        self._verify("/documents")

    def test_feats(self):
        self._verify("/feats")

    def test_magicitems(self):
        self._verify("/magicitems")

    # /manifest is excluded because it's too volatile

    def test_monsters(self):
        self._verify("/monsters")

    def test_planes(self):
        self._verify("/planes")

    def test_races(self):
        self._verify("/races")

    def test_search(self):
        self._verify("/search")

    def test_sections(self):
        self._verify("/sections")

    def test_spelllist(self):
        self._verify("/spelllist")

    def test_spells(self):
        self._verify("/spells")

    def test_weapons(self):
        self._verify("/weapons")

