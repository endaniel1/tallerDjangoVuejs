<template>
	<div class="container">
		<div class="row">
			<div class="col text-left">
				<h2>Nuevo de Libro</h2>
			</div>
		</div>		

		<div class="row">
			<div class="col">
				<div class="card">
					<div class="card-body">
						<form @submit.prevent="submit">		
							<div class="form-group row">
								<label for="title" class="col-sm-2 col-form-label">Titulo</label>
								<div class="col-sm-6">
									<input type="text" name="title" placeholder="Titulo" class="form-control" v-model.trim="form.title">
								</div>
							</div>		
							<div class="form-group row">
								<label for="description" class="col-sm-2 col-form-label">Descripción</label>
								<div class="col-sm-6">
									<textarea name="description" class="form-control" placeholder="Descripción" rows="3" v-model.trim="form.description"></textarea>
								</div>
							</div>

							<div class="row">
								<div class="col text-left">
									<b-button type="submit" variant="primary">
										Crear
									</b-button>
									<b-button type="button" class="btn-large-space" :to="{ name : 'ListBook' }">
										Cancelar
									</b-button>
								</div>
							</div>
						</form>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>
<script>
	import axios from 'axios'
	import swal from 'sweetalert'

	export default {
		created(){
		},
		data(){
			return {
				form: {
					title: "",
					description: ""
				}
			}
		},
		methods: {
			submit(){
				let path = `${process.env.BASE_URI}books/`

				axios.post(path, this.form).then((response) => {
					this.form.title = response.data.title
					this.form.description = response.data.description
					
					swal("Libro Creado Existosamente..!", "", "success")
				})
				.catch((error) => {
					swal("Libro No Creado..!", "", "error")
				})
			}
		}
	}	
</script>