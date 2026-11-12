import unittest

from app import app, tasks


class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True)
        tasks.clear()
        self.client = app.test_client()

    def tearDown(self):
        tasks.clear()

    def test_add_task_trims_input(self):
        response = self.client.post('/add_task', data={'task': '  Review code  '})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(tasks, ['Review code'])

    def test_blank_or_oversized_tasks_are_not_added(self):
        self.client.post('/add_task', data={'task': '   '})
        self.client.post('/add_task', data={'task': 'x' * 201})

        self.assertEqual(tasks, [])

    def test_remove_task_uses_post(self):
        tasks.append('Review code')

        get_response = self.client.get('/remove_task/0')
        post_response = self.client.post('/remove_task/0')

        self.assertEqual(get_response.status_code, 405)
        self.assertEqual(post_response.status_code, 302)
        self.assertEqual(tasks, [])

    def test_invalid_remove_index_does_not_change_tasks(self):
        tasks.append('Review code')

        response = self.client.post('/remove_task/5')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(tasks, ['Review code'])


if __name__ == '__main__':
    unittest.main()
