# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import tests
import webtest

from . import datastore


class TestNamespaceDatastoreSample(tests.AppEngineTestbedCase):

    def setUp(self):
        super(TestNamespaceDatastoreSample, self).setUp()
        self.app = webtest.TestApp(datastore.app)

    def test_get(self):
        response = self.app.get('/datastore')
        self.assertEqual(response.status_int, 200)
        self.assertTrue('Global: 1' in response.body)

        response = self.app.get('/datastore/a')
        self.assertEqual(response.status_int, 200)
        self.assertTrue('Global: 2' in response.body)
        self.assertTrue('a: 1' in response.body)

        response = self.app.get('/datastore/b')
        self.assertEqual(response.status_int, 200)
        self.assertTrue('Global: 3' in response.body)
        self.assertTrue('b: 1' in response.body)
