from django.test import TestCase, Client
from django.urls import reverse


class ProjectsViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_projects_page_returns_200(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)

    def test_projects_page_uses_correct_template(self):
        response = self.client.get(reverse('projects'))
        self.assertTemplateUsed(response, 'projects/projects.html')

    def test_projects_page_context_contains_projects(self):
        response = self.client.get(reverse('projects'))
        self.assertIn('projects', response.context)
        self.assertEqual(len(response.context['projects']), 3)

    def test_projects_page_context_contains_page(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.context['page'], 'projects')

    def test_projects_page_context_contains_number(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.context['number'], 9)


class ProjectDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_project_detail_returns_200(self):
        response = self.client.get(reverse('project', args=['1']))
        self.assertEqual(response.status_code, 200)

    def test_project_detail_uses_correct_template(self):
        response = self.client.get(reverse('project', args=['1']))
        self.assertTemplateUsed(response, 'projects/single-project.html')

    def test_project_detail_shows_correct_project(self):
        response = self.client.get(reverse('project', args=['2']))
        self.assertEqual(response.context['project']['title'], 'Portfolio Website')

    def test_project_detail_invalid_id_returns_none(self):
        response = self.client.get(reverse('project', args=['999']))
        self.assertIsNone(response.context['project'])