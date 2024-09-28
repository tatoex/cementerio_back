from .models import Auditoria

class AutitoriaManager:
    def __init__(self, instance, model_name, user=None):
        self.instance = instance
        self.model_name = model_name
        self.user = user or instance.modified_by

    def obtener_cambios(self):
        """Compara los valores del objeto actualizado con los calores previos a su actualizacion en la bases de datos. 
           devuelve los cambios de los ca,pos modificados(Valores nuevos y previos a ser modificados)"""
        # si el objeto es nuevo no hay cambios
        if not self.instance.pk:
            return{}
        # recupera el estado anterior del objeto desde la base de datos
        old_instance=self.instance.__class__.objects.get(pk=self.instance.pk)
        # el discionario para guardar los cambios
        cambios={}

        #iteracion de todos los posibles cambios en el objeto
        for field in self.instance.meta.fields:
            nombre_campo=field.name
            valor_antiguo=getattr(old_instance, nombre_campo)
            valor_nuevo=getattr(self.instance, nombre_campo)
            if valor_antiguo !=valor_nuevo:
                cambios[nombre_campo]={'previo':valor_antiguo,'actual':valor_nuevo}
        return cambios
        
    def auditar_accion(self, accion):
        """ Metodo para registrar que accion va auditarse"""

        # diccionario de opciones
        acciones={
            'CREAR':self._auditar_creacion,'MODIFICAR':self._auditar_modificacion,'BORRAR':self._auditar_eliminacion
        }

    def _auditar_creacion(self):
        """Auditar la creacion de un objeto."""

        descripcion_cambios=f"{self.model_name} creado el {self.instance.loadDate}."
        self._crear_registro_auditoria('CREAR', descripcion_cambios)
    
    def _auditar_modificacion(self):
        """Auditar la modificacion de un objeto."""

        descripcion_cambios=f"{self.model_name} modificado el {self.instance.updateDate}. Cambios: {cambios}"
        self._crear_registro_auditoria('MODIFICAR', descripcion_cambios)
    
    def _auditar_eliminacion(self):
        """Auditar la eliminacion de un objeto."""

        descripcion_cambios=f"{self.model_name} eliminado"
        self._crear_registro_auditoria('BORRAR', descripcion_cambios)
    
    def _crear_registro_auditoria(self, accion, descripcion_cambios):
        """crear un registro en el modelo auditoria"""

        Auditoria.objects.create(
            usuario=self.usuario,
            afectado=self.model_name,
            objecto_id=self.isinstance.id,
            accion=accion,
            descripcion_cambios=descripcion_cambios
        )