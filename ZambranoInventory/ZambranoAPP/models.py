from django.db import models

# Create your models here.

class TblCliente(models.Model):
    id_cliente = models.BigIntegerField(db_column='Id_Cliente', primary_key=True)  # Field name made lowercase.
    id_tipocliente = models.ForeignKey('TblClienteTipo', models.DO_NOTHING, db_column='Id_TipoCliente')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=200)  # Field name made lowercase.
    telefono1 = models.CharField(db_column='Telefono1', max_length=20)  # Field name made lowercase.
    telefono2 = models.CharField(db_column='Telefono2', max_length=20)  # Field name made lowercase.
    correo_electronico = models.CharField(db_column='Correo_Electronico', max_length=100)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    identidad = models.CharField(db_column='Identidad', max_length=100)  # Field name made lowercase.
    rtn = models.CharField(db_column='RTN', max_length=100)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=1000)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_cliente'



class TblClienteTipo(models.Model):
    id_tipocliente = models.BigIntegerField(db_column='Id_TipoCliente', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=1000)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=45)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_cliente_tipo'


class TblCompra(models.Model):
    id_compra = models.BigIntegerField(db_column='Id_Compra', primary_key=True)  # Field name made lowercase.
    id_usuario = models.ForeignKey('TblMsUsuario', models.DO_NOTHING, db_column='Id_Usuario')  # Field name made lowercase.
    id_proveedor = models.ForeignKey('TblProveedores', models.DO_NOTHING, db_column='Id_Proveedor')  # Field name made lowercase.
    total_compras = models.DecimalField(db_column='Total_Compras', max_digits=10, decimal_places=0)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    impuesto = models.DateTimeField(db_column='Impuesto')  # Field name made lowercase.
    descripcion = models.CharField(max_length=1000)
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_compra'


class TblCompraDetalle(models.Model):
    id_compra_detalle = models.BigIntegerField(db_column='Id_Compra_Detalle', primary_key=True)  # Field name made lowercase.
    id_compra = models.ForeignKey(TblCompra, models.DO_NOTHING, db_column='Id_Compra')  # Field name made lowercase.
    id_producto = models.ForeignKey('TblProducto', models.DO_NOTHING, db_column='Id_Producto')  # Field name made lowercase.
    cantidad = models.FloatField(db_column='Cantidad')  # Field name made lowercase.
    impuesto = models.DecimalField(db_column='Impuesto', max_digits=10, decimal_places=0)  # Field name made lowercase.
    precio_compra = models.DecimalField(db_column='Precio_Compra', max_digits=10, decimal_places=0)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.CharField(db_column='Fecha_Modificacion', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_compra_detalle'


class TblHistContrasea(models.Model):
    id_hist = models.BigIntegerField(db_column='Id_Hist', primary_key=True)  # Field name made lowercase.
    id_usuario = models.ForeignKey('TblMsUsuario', models.DO_NOTHING, db_column='Id_Usuario')  # Field name made lowercase.
    contrasena = models.CharField(db_column='Contraseña', max_length=100)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_hist_contraseña'


class TblKardex(models.Model):
    id_kardex = models.BigIntegerField(db_column='Id_Kardex', primary_key=True)  # Field name made lowercase.
    id_usuario = models.ForeignKey('TblMsUsuario', models.DO_NOTHING, db_column='Id_Usuario')  # Field name made lowercase.
    id_producto = models.ForeignKey('TblProducto', models.DO_NOTHING, db_column='Id_Producto')  # Field name made lowercase.
    id_tipomovimiento = models.ForeignKey('TblKardexTipoMovimiento', models.DO_NOTHING, db_column='Id_TipoMovimiento')  # Field name made lowercase.
    id_venta = models.ForeignKey('TblVenta', models.DO_NOTHING, db_column='Id_Venta')  # Field name made lowercase.
    id_compra = models.ForeignKey(TblCompra, models.DO_NOTHING, db_column='Id_Compra')  # Field name made lowercase.
    cantidad = models.FloatField(db_column='Cantidad')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=1000)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_kardex'


class TblKardexTipoMovimiento(models.Model):
    id_tipomovimiento = models.BigIntegerField(db_column='Id_TipoMovimiento', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=1000)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=45)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_kardex_tipo_movimiento'


class TblMsBitacora(models.Model):
    id_bitacora = models.BigIntegerField(db_column='Id_Bitacora', primary_key=True)  # Field name made lowercase.
    id_usuario = models.ForeignKey('TblMsUsuario', models.DO_NOTHING, db_column='Id_Usuario')  # Field name made lowercase.
    id_objeto = models.ForeignKey('TblMsObjetos', models.DO_NOTHING, db_column='Id_Objeto')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    accion = models.CharField(db_column='Accion', max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=1000)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ms_bitacora'


class TblMsObjetos(models.Model):
    id_objeto = models.BigIntegerField(db_column='Id_Objeto', primary_key=True)  # Field name made lowercase.
    objeto = models.CharField(db_column='Objeto', max_length=100)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=1000)  # Field name made lowercase.
    tipo_objeto = models.CharField(db_column='Tipo_Objeto', max_length=45)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ms_objetos'


class TblMsParametros(models.Model):
    id_parametro = models.BigIntegerField(db_column='Id_Parametro', primary_key=True)  # Field name made lowercase.
    id_usuario = models.ForeignKey('TblMsUsuario', models.DO_NOTHING, db_column='Id_Usuario')  # Field name made lowercase.
    parametro = models.CharField(db_column='Parametro', max_length=50)  # Field name made lowercase.
    valor = models.CharField(db_column='Valor', max_length=100)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ms_parametros'


class TblMsPermisos(models.Model):
    id_rol = models.ForeignKey('TblMsRoles', models.DO_NOTHING, db_column='Id_Rol')  # Field name made lowercase.
    id_objeto = models.ForeignKey(TblMsObjetos, models.DO_NOTHING, db_column='Id_Objeto')  # Field name made lowercase.
    permiso_insercion = models.CharField(db_column='Permiso_Insercion', max_length=1)  # Field name made lowercase.
    permiso_eliminacion = models.CharField(db_column='Permiso_Eliminacion', max_length=1)  # Field name made lowercase.
    permiso_actualizacion = models.CharField(db_column='Permiso_Actualizacion', max_length=1)  # Field name made lowercase.
    permiso_consultar = models.CharField(db_column='Permiso_Consultar', max_length=1)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ms_permisos'


class TblMsPreguntas(models.Model):
    id_pregunta = models.BigIntegerField(db_column='Id_Pregunta', primary_key=True)  # Field name made lowercase.
    pregunta = models.CharField(db_column='Pregunta', max_length=100)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=45)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ms_preguntas'


class TblMsPreguntasUsuario(models.Model):
    id_pregunta = models.ForeignKey(TblMsPreguntas, models.DO_NOTHING, db_column='Id_Pregunta')  # Field name made lowercase.
    id_usuario = models.ForeignKey('TblMsUsuario', models.DO_NOTHING, db_column='Id_Usuario')  # Field name made lowercase.
    respuesta = models.CharField(db_column='Respuesta', max_length=100)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ms_preguntas_usuario'

class TblMsRoles(models.Model):
    id_rol = models.BigIntegerField(db_column='Id_Rol', primary_key=True)  # Field name made lowercase.
    rol = models.CharField(db_column='Rol', max_length=30)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=45)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=1000)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ms_roles'


class TblMsUsuario(models.Model):
    id_usuario = models.BigIntegerField(db_column='Id_Usuario', primary_key=True)  # Field name made lowercase.
    id_rol = models.ForeignKey(TblMsRoles, models.DO_NOTHING, db_column='Id_Rol')  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=15)  # Field name made lowercase.
    nombre_usuario = models.CharField(db_column='Nombre_Usuario', max_length=100)  # Field name made lowercase.
    estado_usuario = models.CharField(db_column='Estado_Usuario', max_length=100)  # Field name made lowercase.
    contrasena = models.CharField(db_column='Contraseña', max_length=100)  # Field name made lowercase.
    fecha_ultima_conexion = models.DateTimeField(db_column='Fecha_Ultima_Conexion')  # Field name made lowercase.
    primer_ingreso = models.BigIntegerField(db_column='Primer_Ingreso')  # Field name made lowercase.
    fecha_vencimiento = models.DateTimeField(db_column='Fecha_Vencimiento')  # Field name made lowercase.
    correo_electronico = models.CharField(db_column='Correo_Electronico', max_length=50)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.
    preguntas_contestadas = models.CharField(db_column='Preguntas_Contestadas', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ms_usuario'


class TblProducto(models.Model):
    id_producto = models.BigIntegerField(db_column='Id_Producto', primary_key=True)  # Field name made lowercase.
    id_tipoprodcuto = models.ForeignKey('TblProductoTipo', models.DO_NOTHING, db_column='Id_TipoProdcuto')  # Field name made lowercase.
    nombre_producto = models.CharField(db_column='Nombre_Producto', max_length=100)  # Field name made lowercase.
    cantidad = models.FloatField(db_column='Cantidad')  # Field name made lowercase.
    cantidad_maxima = models.FloatField(db_column='Cantidad_Maxima')  # Field name made lowercase.
    cantidad_minima = models.FloatField(db_column='Cantidad_Minima')  # Field name made lowercase.
    unidad_medida = models.FloatField(db_column='Unidad_Medida')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=1000)  # Field name made lowercase.
    excento_impuesto = models.CharField(db_column='Excento_Impuesto', max_length=45)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_producto'


class TblProductoProduccion(models.Model):
    id_producto_produccion = models.BigIntegerField(db_column='Id_Producto_Produccion', primary_key=True)  # Field name made lowercase.
    id_usuario = models.ForeignKey(TblMsUsuario, models.DO_NOTHING, db_column='Id_Usuario')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_producto_produccion'


class TblProductoTerminadoDetalle(models.Model):
    id_producto_terminado_detalle = models.BigIntegerField(db_column='Id_Producto_Terminado_Detalle', primary_key=True)  # Field name made lowercase.
    id_producto_produccion = models.ForeignKey(TblProductoProduccion, models.DO_NOTHING, db_column='Id_Producto_Produccion')  # Field name made lowercase.
    id_producto = models.ForeignKey(TblProducto, models.DO_NOTHING, db_column='Id_Producto')  # Field name made lowercase.
    cantidad = models.FloatField(db_column='Cantidad')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_producto_terminado_detalle'


class TblProductoTipo(models.Model):
    id_tipoproducto = models.BigIntegerField(db_column='Id_TipoProducto', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=1000)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_producto_tipo'


class TblProveedores(models.Model):
    id_proveedor = models.BigIntegerField(db_column='Id_Proveedor', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=1000)  # Field name made lowercase.
    telefono_empresa = models.CharField(db_column='Telefono_Empresa', max_length=45)  # Field name made lowercase.
    telefono_encargado = models.CharField(db_column='Telefono_Encargado', max_length=45)  # Field name made lowercase.
    correo_electronico = models.CharField(db_column='Correo_Electronico', max_length=45)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=50)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_proveedores'


class TblTalonarioCai(models.Model):
    id_talonario = models.BigIntegerField(db_column='Id_Talonario', primary_key=True)  # Field name made lowercase.
    id_usuario = models.ForeignKey(TblMsUsuario, models.DO_NOTHING, db_column='Id_Usuario')  # Field name made lowercase.
    factura = models.CharField(db_column='Factura', max_length=100)  # Field name made lowercase.
    secuencia_actual = models.CharField(db_column='Secuencia_Actual', max_length=50)  # Field name made lowercase.
    secuencia_inicial = models.CharField(db_column='Secuencia_Inicial', max_length=50)  # Field name made lowercase.
    secuencia_final = models.CharField(db_column='Secuencia_Final', max_length=50)  # Field name made lowercase.
    fecha_vencimiento = models.DateTimeField(db_column='Fecha_Vencimiento')  # Field name made lowercase.
    numero_cai = models.IntegerField(db_column='Numero_Cai')  # Field name made lowercase.
    sucursal = models.CharField(db_column='Sucursal', max_length=45)  # Field name made lowercase.
    punto_emision = models.CharField(db_column='Punto_Emision', max_length=45)  # Field name made lowercase.
    tipo_documento = models.CharField(db_column='Tipo_Documento', max_length=45)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=45)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_talonario_cai'


class TblVenta(models.Model):
    id_venta = models.BigIntegerField(db_column='Id_Venta', primary_key=True)  # Field name made lowercase.
    id_cliente = models.ForeignKey(TblCliente, models.DO_NOTHING, db_column='Id_Cliente')  # Field name made lowercase.
    id_usuario = models.ForeignKey(TblMsUsuario, models.DO_NOTHING, db_column='Id_Usuario')  # Field name made lowercase.
    id_ventaestado = models.ForeignKey('TblVentaEstado', models.DO_NOTHING, db_column='Id_VentaEstado')  # Field name made lowercase.
    id_tipopago = models.ForeignKey('TblVentaTipoPago', models.DO_NOTHING, db_column='Id_TipoPago')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    sub_total = models.DecimalField(db_column='Sub_Total', max_digits=10, decimal_places=0)  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=10, decimal_places=0)  # Field name made lowercase.
    impuesto = models.DecimalField(db_column='Impuesto', max_digits=10, decimal_places=0)  # Field name made lowercase.
    total_pagar = models.DecimalField(db_column='Total_Pagar', max_digits=10, decimal_places=0)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=1000)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_venta'


class TblVentaDetalle(models.Model):
    id_venta_detalle = models.BigIntegerField(db_column='Id_venta_detalle', primary_key=True)  # Field name made lowercase.
    id_venta = models.ForeignKey(TblVenta, models.DO_NOTHING, db_column='Id_Venta')  # Field name made lowercase.
    id_producto = models.ForeignKey(TblProducto, models.DO_NOTHING, db_column='Id_Producto')  # Field name made lowercase.
    cantidad = models.FloatField(db_column='Cantidad')  # Field name made lowercase.
    sub_total = models.DecimalField(db_column='Sub_Total', max_digits=10, decimal_places=0)  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=10, decimal_places=0)  # Field name made lowercase.
    impuesto = models.DecimalField(db_column='Impuesto', max_digits=10, decimal_places=0)  # Field name made lowercase.
    total_pagar = models.DecimalField(db_column='Total_Pagar', max_digits=10, decimal_places=0)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_venta_detalle'


class TblVentaEstado(models.Model):
    id_ventaestado = models.BigIntegerField(db_column='Id_VentaEstado', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=1000)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_venta_estado'


class TblVentaTipoPago(models.Model):
    id_tipopago = models.BigIntegerField(db_column='Id_TipoPago', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=45)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado_Por', max_length=15)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion')  # Field name made lowercase.
    modificado_por = models.CharField(db_column='Modificado_Por', max_length=15)  # Field name made lowercase.
    fecha_modificacion = models.DateTimeField(db_column='Fecha_Modificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_venta_tipo_pago'
