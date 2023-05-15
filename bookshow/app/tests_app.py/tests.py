from django.test import TestCase
from rest_framework import status
from django.urls import reverse
import pytest
from model_bakery import baker
from app.models import BookCategory,BookDeatils

@pytest.mark.django_db
class BookTest(TestCase):
    def test_one(self):
        return None

    #----------------------#
    #----Book_Category-----#
    #----------------------#

    def test_create_book_category(self):

        book_category = baker.make(BookCategory)
        url = reverse('category-create')
        user_input = {
        "category_name":book_category.category_name
                    }
        response =self.client.post(

        url, user_input, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_empty_category_name(self):
        book_category = baker.make("BookCategory")
        url = reverse('category-create')
        user_input = {
        "category_name":""
                    }
        response =self.client.post(

        url, user_input, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_book_category_list(self):
        url = reverse('category-list')
        response = self.client.get(
            url, follow=True, content_type="application/json")
        assert response.status_code, status.HTTP_200_OK

    def test_view_specific_book_category(self):
        category = baker.make(BookCategory)
        url = reverse('category-view',args=(category.slug,))
        response = self.client.get(
            url, follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_view_specific_book_category_invalid_slug(self):
        category = baker.make(BookCategory)
        url = reverse('category-view',args=('category',))
        response = self.client.get(
            url, follow=True
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_book_category(self):
            category = baker.make(BookCategory)
            url = reverse('category-update',args=(category.slug,))
            data = {
                "category_name":"mani"
            }
            response = self.client.put(
                url, data=data, content_type="application/json"

            )
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book_category(self):
        category = baker.make(BookCategory)
        url = reverse('category-delete',args=(category.slug,))
        response = self.client.delete(
            url, content_type="application/json"
        )
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)


    # #----------------------#
    # #----Book_Details-----#
    # #----------------------#

    def test_create_book_details(self):

        book_details = baker.make(BookDeatils)
        book_category = baker.make(BookCategory)
        url = reverse('booke-create',args=(book_category.slug,))

        user_input = {
        "title":book_details.title,
        "author_name":book_details.author_name
                            }                    
        response =self.client.post(
        url, user_input, content_type="multipart/form-data")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_view_book_details(self):
        url = reverse('book-list')
        response = self.client.get(
            url, follow=True, content_type="application/json")
        assert response.status_code, status.HTTP_200_OK

    def test_delete_book_details(self):
        bookDeatils = baker.make(BookDeatils)
        url = reverse('book-delete',args=(bookDeatils.slug,))
        response = self.client.delete(
            url, content_type="application/json"
        )
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)


    
    def test_delete_book_details_invalid_slug(self):
        bookDeatils = baker.make(BookDeatils)
        url = reverse('book-delete',args=("bookDeatils",))
        response = self.client.delete(
            url, content_type="application/json"
        )
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)


     
        