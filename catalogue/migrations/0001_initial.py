# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 17:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlobularCluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster_id', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Alternative names')),
                ('ra', models.FloatField(blank=True, null=True, verbose_name='Right ascension (seconds)')),
                ('dec', models.FloatField(blank=True, null=True, verbose_name='Declinations (seconds)')),
                ('gallon', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('gallat', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
                ('dfs', models.FloatField(blank=True, null=True, verbose_name='Distance from the sun')),
                ('dfs_unit', models.CharField(blank=True, default='pc', max_length=32, null=True, verbose_name='Units')),
                ('dfgc', models.FloatField(blank=True, null=True, verbose_name='Distance from galactic center')),
                ('dfgc_unit', models.CharField(blank=True, default='pc', max_length=32, null=True, verbose_name='Units')),
                ('dfgc_x', models.FloatField(blank=True, null=True, verbose_name='Coordinate X')),
                ('dfgc_y', models.FloatField(blank=True, null=True, verbose_name='Coordinate Y')),
                ('dfgc_z', models.FloatField(blank=True, null=True, verbose_name='Coordinate Z')),
                ('metallicity', models.FloatField(blank=True, null=True, verbose_name='Metallicity')),
                ('w_mean_met', models.FloatField(blank=True, null=True, verbose_name='Weight of mean metallicity')),
                ('eb_v', models.FloatField(blank=True, null=True, verbose_name='Foreground reddening E(B-V)')),
                ('v_hb', models.FloatField(blank=True, null=True, verbose_name='V magnitude level of horizontal branch')),
                ('app_vd_mod', models.FloatField(blank=True, null=True, verbose_name='Apparent visual magnitude modulus')),
                ('v_t', models.FloatField(blank=True, null=True, verbose_name='Integrated V magnitud, v_t')),
                ('m_v_t', models.FloatField(blank=True, null=True, verbose_name='Cluster luminosity')),
                ('ph_u_b', models.FloatField(blank=True, null=True, verbose_name='U-B')),
                ('ph_b_v', models.FloatField(blank=True, null=True, verbose_name='B-V')),
                ('ph_v_r', models.FloatField(blank=True, null=True, verbose_name='V-R')),
                ('ph_v_i', models.FloatField(blank=True, null=True, verbose_name='V-I')),
                ('spt', models.CharField(blank=True, max_length=3, null=True, verbose_name='Spectral type')),
                ('ellipticity', models.FloatField(blank=True, null=True, verbose_name='Projected ellipticity of isophotes')),
                ('v_r', models.FloatField(blank=True, null=True, verbose_name='Heliocentric radial velocity')),
                ('v_r_err', models.FloatField(blank=True, null=True, verbose_name='Observational uncertainty')),
                ('v_r_unit', models.CharField(blank=True, default='km/s', max_length=32, verbose_name='Units')),
                ('c_LSR', models.FloatField(blank=True, null=True, verbose_name='Radial velocity wrt the solar neighbourhood')),
                ('c_LSR_unit', models.CharField(blank=True, default='km/s', max_length=32, verbose_name='Units')),
                ('sig_v', models.FloatField(blank=True, null=True, verbose_name='Velocity dispersion')),
                ('sig_err', models.FloatField(blank=True, null=True, verbose_name='Observational uncertainty')),
                ('sig_v_unit', models.CharField(blank=True, default='km/s', max_length=32, verbose_name='Units')),
                ('sp_c', models.FloatField(blank=True, null=True, verbose_name='King-model central concentration')),
                ('sp_r_c', models.FloatField(blank=True, null=True, verbose_name='Core radius')),
                ('sp_r_c_unit', models.CharField(blank=True, default='arcmin', max_length=32, verbose_name='Units')),
                ('sp_r_h', models.FloatField(blank=True, null=True, verbose_name='Half-light radius')),
                ('sp_r_h_unit', models.CharField(blank=True, default='arcmin', max_length=32, verbose_name='Units')),
                ('sp_mu_V', models.FloatField(blank=True, null=True, verbose_name='Central surface brightness')),
                ('sp_mu_V_unit', models.CharField(blank=True, default='V mag/arcsec^2', max_length=32, verbose_name='Units')),
                ('sp_rho_0', models.FloatField(blank=True, null=True, verbose_name='Central luminosity density')),
                ('sp_rho_0_unit', models.CharField(blank=True, default='L\u2609/pc^3', max_length=32, verbose_name='Units')),
                ('sp_lg_tc', models.FloatField(blank=True, null=True, verbose_name='Core relaxation time')),
                ('sp_lg_th', models.FloatField(blank=True, null=True, verbose_name='Mean relaxation time')),
                ('sp_t_unit', models.CharField(blank=True, default='log10(yr)', max_length=32, verbose_name='Units')),
                ('cluster_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.GlobularCluster')),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, null=True)),
                ('doi', models.CharField(blank=True, max_length=256, null=True)),
                ('ads', models.CharField(blank=True, max_length=256, null=True)),
                ('pub_date', models.DateField(null=True, verbose_name='publication date')),
            ],
        ),
        migrations.AddField(
            model_name='observation',
            name='ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Reference'),
        ),
    ]