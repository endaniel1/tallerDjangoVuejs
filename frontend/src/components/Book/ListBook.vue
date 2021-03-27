<template>
	<div class="container">
		<div class="row">
			<div class="col text-left">
				<div class="">					
					<h2>Listado de Libro</h2>
					<b-button size="sms" :to="{ name : 'CreateBook' }" variant="success">
						Nuevo Libro
					</b-button>
				</div>
				<br>
				<div class="col-md-12">
					<b-table striped hover :items="books" :fields="fields">

						<template  #cell(action)="data">
							<b-button size="sm" variant="primary" 
							:to="{ name : 'EditBook', params : { bookId : data.item.id } }">
								Editar
							</b-button>
							<b-button size="sm" variant="danger"
							:to="{ name : 'DeleteBook', params : { bookId : data.item.id } }">
								Eliminar
							</b-button>
						</template>

					</b-table>
				</div>
			</div>
		</div>
	</div>
</template>
<script>
	import axios from 'axios'

	export default {
		created(){
			this.getBooks();
		},
		data(){
			return {
				fields: [
					{ key: "title", label: "Titulo" },
					{ key: "description", label: "Descripción" },
					{ key: "action", label: "Acciones" },
				],
				books: []
			}
		},
		methods: {
			getBooks (){
				let path = `${process.env.BASE_URI}books/`

				axios.get(path).then((response) =>{
					this.books = response.data
				})
				.catch((error) => {
					console.log(error)
				})
			}
		}
	}	
</script>