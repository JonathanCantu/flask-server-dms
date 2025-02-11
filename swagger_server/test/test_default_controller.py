# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.album import Album  # noqa: E501
from swagger_server.models.artist import Artist  # noqa: E501
from swagger_server.models.customer import Customer  # noqa: E501
from swagger_server.models.employee import Employee  # noqa: E501
from swagger_server.models.genre import Genre  # noqa: E501
from swagger_server.models.invoice import Invoice  # noqa: E501
from swagger_server.models.invoice_line import InvoiceLine  # noqa: E501
from swagger_server.models.media_type import MediaType  # noqa: E501
from swagger_server.models.playlist import Playlist  # noqa: E501
from swagger_server.models.playlist_track import PlaylistTrack  # noqa: E501
from swagger_server.models.track import Track  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_album_id_get(self):
        """Test case for album_id_get

        Returns an album.
        """
        response = self.client.open(
            '/album/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_album_post(self):
        """Test case for album_post

        Create an album.
        """
        body = Album()
        response = self.client.open(
            '/album',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_album_put(self):
        """Test case for album_put

        Updates an album
        """
        body = Album()
        response = self.client.open(
            '/album',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_artist_id_get(self):
        """Test case for artist_id_get

        Returns an artist.
        """
        response = self.client.open(
            '/artist/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_artist_post(self):
        """Test case for artist_post

        Create an artist.
        """
        body = Artist()
        response = self.client.open(
            '/artist',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_artist_put(self):
        """Test case for artist_put

        Returns an updated artist.
        """
        body = Artist()
        response = self.client.open(
            '/artist',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_customer_id_get(self):
        """Test case for customer_id_get

        Returns a customer.
        """
        response = self.client.open(
            '/customer/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_customer_post(self):
        """Test case for customer_post

        Returns a newly created customer record.
        """
        body = Customer()
        response = self.client.open(
            '/customer',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_customer_put(self):
        """Test case for customer_put

        Returns an updated customer record.
        """
        body = Customer()
        response = self.client.open(
            '/customer',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_employee_id_get(self):
        """Test case for employee_id_get

        Returns an employee record.
        """
        response = self.client.open(
            '/employee/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_employee_post(self):
        """Test case for employee_post

        Returns a newly created employee record.
        """
        body = Employee()
        response = self.client.open(
            '/employee',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_employee_put(self):
        """Test case for employee_put

        Returns an updated employee record.
        """
        body = Employee()
        response = self.client.open(
            '/employee',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_genre_id_get(self):
        """Test case for genre_id_get

        Returns a genre.
        """
        response = self.client.open(
            '/genre/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_genre_post(self):
        """Test case for genre_post

        Create a genre.
        """
        body = Genre()
        response = self.client.open(
            '/genre',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_genre_put(self):
        """Test case for genre_put

        Returns an updated genre.
        """
        body = Genre()
        response = self.client.open(
            '/genre',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoice_id_get(self):
        """Test case for invoice_id_get

        Returns an invoice.
        """
        response = self.client.open(
            '/invoice/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoice_post(self):
        """Test case for invoice_post

        Returns an invoice.
        """
        body = Invoice()
        response = self.client.open(
            '/invoice',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoice_put(self):
        """Test case for invoice_put

        Returns an updated invoice.
        """
        body = Invoice()
        response = self.client.open(
            '/invoice',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoiceline_id_get(self):
        """Test case for invoiceline_id_get

        Returns a line from an invoice
        """
        response = self.client.open(
            '/invoiceline/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoiceline_post(self):
        """Test case for invoiceline_post

        Create a invoice line item
        """
        body = InvoiceLine()
        response = self.client.open(
            '/invoiceline',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invoiceline_put(self):
        """Test case for invoiceline_put

        Update invoice line
        """
        body = InvoiceLine()
        response = self.client.open(
            '/invoiceline',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mediatype_id_get(self):
        """Test case for mediatype_id_get

        Returns a media type.
        """
        response = self.client.open(
            '/mediatype/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mediatype_post(self):
        """Test case for mediatype_post

        Create a media type.
        """
        body = MediaType()
        response = self.client.open(
            '/mediatype',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mediatype_put(self):
        """Test case for mediatype_put

        Update a media type
        """
        body = MediaType()
        response = self.client.open(
            '/mediatype',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_playlist_id_delete(self):
        """Test case for playlist_id_delete

        Delete playlist
        """
        response = self.client.open(
            '/playlist/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_playlist_id_get(self):
        """Test case for playlist_id_get

        Returns a playlist
        """
        response = self.client.open(
            '/playlist/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_playlist_post(self):
        """Test case for playlist_post

        Create a playlist.
        """
        body = Playlist()
        response = self.client.open(
            '/playlist',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_playlist_put(self):
        """Test case for playlist_put

        Returns a modified playlist
        """
        body = Playlist()
        response = self.client.open(
            '/playlist',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_playlisttrack_id_delete(self):
        """Test case for playlisttrack_id_delete

        Deletes a playlist track
        """
        response = self.client.open(
            '/playlisttrack/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_playlisttrack_id_get(self):
        """Test case for playlisttrack_id_get

        Returns a playlist track
        """
        response = self.client.open(
            '/playlisttrack/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_playlisttrack_post(self):
        """Test case for playlisttrack_post

        Create a playlist track.
        """
        body = PlaylistTrack()
        response = self.client.open(
            '/playlisttrack',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_playlisttrack_put(self):
        """Test case for playlisttrack_put

        Updates a playlist track
        """
        body = PlaylistTrack()
        response = self.client.open(
            '/playlisttrack',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_track_id_get(self):
        """Test case for track_id_get

        Returns a song track
        """
        response = self.client.open(
            '/track/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_track_post(self):
        """Test case for track_post

        Create a song track.
        """
        body = Track()
        response = self.client.open(
            '/track',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_track_put(self):
        """Test case for track_put

        Updates a song track
        """
        body = Track()
        response = self.client.open(
            '/track',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
