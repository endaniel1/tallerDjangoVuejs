import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import ListBook from '@/components/Book/ListBook'
import EditBook from '@/components/Book/EditBook'
import DeleteBook from '@/components/Book/DeleteBook'
import CreateBook from '@/components/Book/CreateBook'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/books',
      name: 'ListBook',
      component: ListBook
    },
    {
      path: '/books/create',
      name: 'CreateBook',
      component: CreateBook
    },
    {
      path: '/books/:bookId/edit',
      name: 'EditBook',
      component: EditBook
    },
    {
      path: '/books/:bookId/delete',
      name: 'DeleteBook',
      component: DeleteBook
    }
  ],
  mode: 'history'
})
