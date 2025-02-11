import connexion
import six

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
from swagger_server import util


def album_id_get(id):  # noqa: E501
    """Returns an album.

     # noqa: E501

    :param id: Album ID
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def album_post(body=None):  # noqa: E501
    """Create an album.

     # noqa: E501

    :param body: Create album
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Album.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def album_put(body=None):  # noqa: E501
    """Updates an album

     # noqa: E501

    :param body: Update album
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Album.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def artist_id_get(id):  # noqa: E501
    """Returns an artist.

     # noqa: E501

    :param id: Artist ID
    :type id: int

    :rtype: Artist
    """
    return 'do some magic!'


def artist_post(body=None):  # noqa: E501
    """Create an artist.

     # noqa: E501

    :param body: Create artist
    :type body: dict | bytes

    :rtype: Artist
    """
    if connexion.request.is_json:
        body = Artist.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def artist_put(body=None):  # noqa: E501
    """Returns an updated artist.

     # noqa: E501

    :param body: Update artist
    :type body: dict | bytes

    :rtype: Artist
    """
    if connexion.request.is_json:
        body = Artist.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def customer_id_get(id):  # noqa: E501
    """Returns a customer.

     # noqa: E501

    :param id: Customer ID
    :type id: int

    :rtype: Customer
    """
    return 'do some magic!'


def customer_post(body=None):  # noqa: E501
    """Returns a newly created customer record.

     # noqa: E501

    :param body: Create customer
    :type body: dict | bytes

    :rtype: Customer
    """
    if connexion.request.is_json:
        body = Customer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def customer_put(body=None):  # noqa: E501
    """Returns an updated customer record.

     # noqa: E501

    :param body: Update customer
    :type body: dict | bytes

    :rtype: Customer
    """
    if connexion.request.is_json:
        body = Customer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def employee_id_get(id):  # noqa: E501
    """Returns an employee record.

     # noqa: E501

    :param id: Employee ID
    :type id: int

    :rtype: Employee
    """
    return 'do some magic!'


def employee_post(body=None):  # noqa: E501
    """Returns a newly created employee record.

     # noqa: E501

    :param body: Create an employee
    :type body: dict | bytes

    :rtype: Employee
    """
    if connexion.request.is_json:
        body = Employee.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def employee_put(body=None):  # noqa: E501
    """Returns an updated employee record.

     # noqa: E501

    :param body: Update employee
    :type body: dict | bytes

    :rtype: Employee
    """
    if connexion.request.is_json:
        body = Employee.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def genre_id_get(id):  # noqa: E501
    """Returns a genre.

     # noqa: E501

    :param id: Genre ID
    :type id: int

    :rtype: Genre
    """
    return 'do some magic!'


def genre_post(body=None):  # noqa: E501
    """Create a genre.

     # noqa: E501

    :param body: Create genre
    :type body: dict | bytes

    :rtype: Genre
    """
    if connexion.request.is_json:
        body = Genre.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def genre_put(body=None):  # noqa: E501
    """Returns an updated genre.

     # noqa: E501

    :param body: Update genre
    :type body: dict | bytes

    :rtype: Genre
    """
    if connexion.request.is_json:
        body = Genre.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def invoice_id_get(id):  # noqa: E501
    """Returns an invoice.

     # noqa: E501

    :param id: Invoice ID
    :type id: int

    :rtype: Invoice
    """
    return 'do some magic!'


def invoice_post(body=None):  # noqa: E501
    """Returns an invoice.

     # noqa: E501

    :param body: Create invoice
    :type body: dict | bytes

    :rtype: Invoice
    """
    if connexion.request.is_json:
        body = Invoice.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def invoice_put(body=None):  # noqa: E501
    """Returns an updated invoice.

     # noqa: E501

    :param body: Update invoice
    :type body: dict | bytes

    :rtype: Invoice
    """
    if connexion.request.is_json:
        body = Invoice.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def invoiceline_id_get(id):  # noqa: E501
    """Returns a line from an invoice

     # noqa: E501

    :param id: Invoice Line ID
    :type id: int

    :rtype: InvoiceLine
    """
    return 'do some magic!'


def invoiceline_post(body=None):  # noqa: E501
    """Create a invoice line item

     # noqa: E501

    :param body: Create invoice line item
    :type body: dict | bytes

    :rtype: InvoiceLine
    """
    if connexion.request.is_json:
        body = InvoiceLine.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def invoiceline_put(body=None):  # noqa: E501
    """Update invoice line

     # noqa: E501

    :param body: Update invoice line
    :type body: dict | bytes

    :rtype: InvoiceLine
    """
    if connexion.request.is_json:
        body = InvoiceLine.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def mediatype_id_get(id):  # noqa: E501
    """Returns a media type.

     # noqa: E501

    :param id: Media Type ID
    :type id: int

    :rtype: MediaType
    """
    return 'do some magic!'


def mediatype_post(body=None):  # noqa: E501
    """Create a media type.

     # noqa: E501

    :param body: Create media type
    :type body: dict | bytes

    :rtype: MediaType
    """
    if connexion.request.is_json:
        body = MediaType.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def mediatype_put(body=None):  # noqa: E501
    """Update a media type

     # noqa: E501

    :param body: Update media type
    :type body: dict | bytes

    :rtype: MediaType
    """
    if connexion.request.is_json:
        body = MediaType.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def playlist_id_delete(id):  # noqa: E501
    """Delete playlist

     # noqa: E501

    :param id: Playlist ID
    :type id: int

    :rtype: Playlist
    """
    return 'do some magic!'


def playlist_id_get(id):  # noqa: E501
    """Returns a playlist

     # noqa: E501

    :param id: Playlist ID
    :type id: int

    :rtype: Playlist
    """
    return 'do some magic!'


def playlist_post(body=None):  # noqa: E501
    """Create a playlist.

     # noqa: E501

    :param body: Create playlist
    :type body: dict | bytes

    :rtype: Playlist
    """
    if connexion.request.is_json:
        body = Playlist.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def playlist_put(body=None):  # noqa: E501
    """Returns a modified playlist

     # noqa: E501

    :param body: Update playlist
    :type body: dict | bytes

    :rtype: Playlist
    """
    if connexion.request.is_json:
        body = Playlist.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def playlisttrack_id_delete(id):  # noqa: E501
    """Deletes a playlist track

     # noqa: E501

    :param id: Playlist Track ID
    :type id: int

    :rtype: PlaylistTrack
    """
    return 'do some magic!'


def playlisttrack_id_get(id):  # noqa: E501
    """Returns a playlist track

     # noqa: E501

    :param id: Playlist Track ID
    :type id: int

    :rtype: PlaylistTrack
    """
    return 'do some magic!'


def playlisttrack_post(body=None):  # noqa: E501
    """Create a playlist track.

     # noqa: E501

    :param body: Create playlist track
    :type body: dict | bytes

    :rtype: PlaylistTrack
    """
    if connexion.request.is_json:
        body = PlaylistTrack.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def playlisttrack_put(body=None):  # noqa: E501
    """Updates a playlist track

     # noqa: E501

    :param body: Update playlist track
    :type body: dict | bytes

    :rtype: PlaylistTrack
    """
    if connexion.request.is_json:
        body = PlaylistTrack.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def track_id_get(id):  # noqa: E501
    """Returns a song track

     # noqa: E501

    :param id: Track ID
    :type id: int

    :rtype: Track
    """
    return 'do some magic!'


def track_post(body=None):  # noqa: E501
    """Create a song track.

     # noqa: E501

    :param body: Create song track
    :type body: dict | bytes

    :rtype: Track
    """
    if connexion.request.is_json:
        body = Track.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def track_put(body=None):  # noqa: E501
    """Updates a song track

     # noqa: E501

    :param body: Update song track
    :type body: dict | bytes

    :rtype: Track
    """
    if connexion.request.is_json:
        body = Track.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
