#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
import datetime
from google.appengine.ext import ndb
from google.appengine.api import users

class Person(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    school = ndb.StringProperty()

class Photo(ndb.Model):
    image = ndb.BlobProperty()
    created = ndb.DateTimeProperty()
    owner = ndb.UserProperty()
    location = ndb.GeoPtProperty()
    views = ndb.IntegerProperty()
    caption = ndb.StringProperty()
    camera_type = ndb.StringProperty()
    people_in_photo = ndb.KeyProperty(Person, repeated=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            greeting = 'Welcome, {}! (<a href="{}">Sign out</a>)'.format(nickname, logout_url)
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)
        self.response.write('<html><body>{}</body></html>'.format(greeting))

class AddPersonPage(webapp2.RequestHandler):
    def get (self):
        me = Person(name='Jasmine Chin', email='jasminechin0412@gmail.com', school='SBU')
        my_key = me.put()
        self.response.write(my_key.id())

class TagPersonInPhotoPage(webapp2.RequestHandler):
    def get(self):
        photo_id = int(self.request.get('photo_id'))
        person_id = int(self.request.get('person_id'))
        this_photo = Photo.get_by_id(photo_id)
        this_person = Person.get_by_id(person_id)
        people = this_photo.people_in_photo
        if this_person.key in people:
            return
        this_photo.people_in_photo.append(this_person.key)
        this_photo.put()
        self.response.write('Person %d tagged in photo %d' % (person_id, photo_id))

class AddPhotoPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        my_photo = Photo(image='dajslkdjaslkd', created=datetime.datetime.now(), owner=user,
                         location=ndb.GeoPt("52.37, 4.88"), views=0, caption="This is a photo.", camera_type="Pixel", people_in_photo=[])
        key = my_photo.put()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(key.id())

class GetPhotoPage(webapp2.RequestHandler):
    def get(self):
        photo_id = int(self.request.get('id'))
        my_photo = Photo.get_by_id(photo_id)
        self.response.write(my_photo.caption)

class DeletePhotoPage(webapp2.RequestHandler):
    def get(self):
        photo_id = int(self.request.get('id'))
        my_photo = Photo.get_by_id(photo_id)
        my_photo.delete()

class ListPhotoPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h2>Most recent 5 photos</h2>')
        results = Photo.query().order(-Photo.created).fetch(limit=5)
        for result in results:
            self.response.write('<p>Photo id is %d and photo caption is "%s"</p>' % (result.key.id(), result.caption))

        self.response.write('<h2>All iPhone photos</h2>')
        results = Photo.query(Photo.camera_type=='iPhone').fetch(limit=5)
        for result in results:
            self.response.write('<p>Photo id is %d and photo caption is "%s"</p>' % (result.key.id(), result.caption))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/addperson', AddPersonPage),
    ('/addphoto', AddPhotoPage),
    ('/getphoto', GetPhotoPage),
    ('/deletephoto', DeletePhotoPage),
    ('/listphoto', ListPhotoPage),
    ('/tag', TagPersonInPhotoPage)
], debug=True)
