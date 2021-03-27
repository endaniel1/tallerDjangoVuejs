<template>
	<div class="container">
		<div class="row">
			<div class="col">
				<h3>¿Esta Seguro de Eliminar el Libro?</h3>
				<p>Titulo: {{ this.element.title }}</p>
				<p>Descripción: {{ this.element.description }}</p>
			</div>
		</div>
		<div class="row">
			<div class="col"e>				
				<b-button v-on:click="deleteBook" variant="danger">
					Sí, Eliminar.
				</b-button>
			</div>
		</div>
	</div>
</template>
<script>
	import axios from 'axios'
	import swal from 'sweetalert'

	export default {
		created(){
			this.getBook()
		},
		data(){
			return {
				bookId: this.$route.params.bookId,
				element: {
					title: "",
					description: ""
				}
			}
		},
		methods: {
			getBook(){				
				let path = `${process.env.BASE_URI}books/${this.bookId}/`

				axios.get(path).then((response) => {
					this.element.title = response.data.title
					this.element.description = response.data.description
				})
				.catch((error) => {
					console.log(error)
				})
			},
			deleteBook(){	
				let path = `${process.env.BASE_URI}books/${this.bookId}/`

				axios.delete(path).then((response) => {
					location.href = '/books'
				})
				.catch((error) => {
					swal("No Es Posible Eliminar El Libro..!!", "", "error")
				})
			}
		}
	}
</script>