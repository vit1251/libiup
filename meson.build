project('libiup', 'c', version: '3.28')

dependencies = []

inc_dir = include_directories('include', 'src')

driver = get_option('DRIVER')

cc = meson.get_compiler('c')

m_dep = cc.find_library('m')
dependencies += m_dep

gtk_dep = dependency('gtk+-3.0')
dependencies += gtk_dep

x11_dep = dependency('x11')
dependencies += x11_dep

# Windows XP minimum
#WIN32VER = 0x0501
#For the future use 0x0601  (Windows 7 minimum)

# Draw driver with alpha and anti-aliasing in Windows and Linux enabled
USE_NEW_DRAW = true

sources = [
    'src/iup_array.c',
    'src/iup_callback.c',
    'src/iup_dlglist.c',
    'src/iup_attrib.c',
    'src/iup_focus.c',
    'src/iup_font.c',
    'src/iup_globalattrib.c',
    'src/iup_object.c',
    'src/iup_key.c',
    'src/iup_layout.c',
    'src/iup_ledlex.c',
    'src/iup_names.c',
    'src/iup_ledparse.c',
    'src/iup_predialogs.c',
    'src/iup_register.c',
    'src/iup_scanf.c',
    'src/iup_show.c',
    'src/iup_str.c',
    'src/iup_func.c',
    'src/iup_childtree.c',
    'src/iup.c',
    'src/iup_classattrib.c',
    'src/iup_dialog.c',
    'src/iup_assert.c',
    'src/iup_messagedlg.c',
    'src/iup_timer.c',
    'src/iup_image.c',
    'src/iup_label.c',
    'src/iup_fill.c',
    'src/iup_zbox.c',
    'src/iup_colordlg.c',
    'src/iup_fontdlg.c',
    'src/iup_filedlg.c',
    'src/iup_strmessage.c',
    'src/iup_menu.c',
    'src/iup_frame.c',
    'src/iup_user.c',
    'src/iup_button.c',
    'src/iup_radio.c',
    'src/iup_toggle.c',
    'src/iup_progressbar.c',
    'src/iup_text.c',
    'src/iup_val.c',
    'src/iup_box.c',
    'src/iup_hbox.c',
    'src/iup_vbox.c',
    'src/iup_cbox.c',
    'src/iup_class.c',
    'src/iup_classbase.c',
    'src/iup_maskmatch.c',
    'src/iup_mask.c',
    'src/iup_maskparse.c',
    'src/iup_tabs.c',
    'src/iup_spin.c',
    'src/iup_list.c',
    'src/iup_getparam.c',
    'src/iup_link.c',
    'src/iup_sbox.c',
    'src/iup_scrollbox.c',
    'src/iup_normalizer.c',
    'src/iup_tree.c',
    'src/iup_split.c',
    'src/iup_layoutdlg.c',
    'src/iup_recplay.c',
    'src/iup_progressdlg.c',
    'src/iup_expander.c',
    'src/iup_open.c',
    'src/iup_table.c',
    'src/iup_canvas.c',
    'src/iup_gridbox.c',
    'src/iup_detachbox.c',
    'src/iup_backgroundbox.c',
    'src/iup_linefile.c',
    'src/iup_config.c',
    'src/iup_flatbutton.c',
    'src/iup_animatedlabel.c',
    'src/iup_draw.c',
    'src/iup_flatframe.c',
    'src/iup_flattabs.c',
    'src/iup_flatscrollbar.c',
    'src/iup_flatscrollbox.c',
    'src/iup_gauge.c',
    'src/iup_dial.c',
    'src/iup_colorbar.c',
    'src/iup_colorbrowser.c',
    'src/iup_colorhsi.c',
    'src/iup_flatlabel.c',
    'src/iup_dropbutton.c',
    'src/iup_flattoggle.c',
    'src/iup_flatseparator.c',
    'src/iup_space.c',
    'src/iup_multibox.c',
    'src/iup_flatlist.c',
    'src/iup_globalsdlg.c',
    'src/iup_flatval.c',
    'src/iup_loop.c',
    'src/iup_thread.c',
    'src/iup_classinfo.c',
    'src/iup_elempropdlg.c',
    'src/iup_export.c',
]

if driver == 'GTK'
#  DEFINES += GTK_DISABLE_DEPRECATED 
#  ifdef USE_GTK3
#    DEFINES += GDK_DISABLE_DEPRECATED
#    DEFINES += GSEAL_ENABLE
#  endif
#  INCLUDES += gtk
sources += [
    'src/gtk/iupgtk_focus.c',
    'src/gtk/iupgtk_clipboard.c',
    'src/gtk/iupgtk_val.c',
    'src/gtk/iupgtk_globalattrib.c',
    'src/gtk/iupgtk_key.c',
    'src/gtk/iupgtk_tips.c',
    'src/gtk/iupgtk_loop.c',
    'src/gtk/iupgtk_open.c',
    'src/gtk/iupgtk_messagedlg.c',
    'src/gtk/iupgtk_timer.c',
    'src/gtk/iupgtk_label.c',
    'src/gtk/iupgtk_font.c',
    'src/gtk/iupgtk_fontdlg.c',
    'src/gtk/iupgtk_filedlg.c',
    'src/gtk/iupgtk_button.c',
    'src/gtk/iupgtk_toggle.c',
    'src/gtk/iupgtk_dragdrop.c',
    'src/gtk/iupgtk_text.c',
    'src/gtk/iupgtk_frame.c',
    'src/gtk/iupgtk_progressbar.c',
    'src/gtk/iupgtk_tabs.c',
    'src/gtk/iupgtk_list.c',
    'src/gtk/iupgtk_tree.c',
    'src/gtk/iupgtk_canvas.c',
    'src/gtk/iupgtk_image.c',
    'src/gtk/iupgtk_dialog.c',
    'src/gtk/iupgtk_common.c',
    'src/gtk/iupgtk_str.c',
    'src/gtk/iupgtk_menu.c',
    'src/gtk/iupgtk_calendar.c',
    'src/iup_datepick.c',
    'src/gtk/iupgtk_help.c',
]

sources += 'src/mot/iupunix_info.c'

USE_GTK3 = true

  if USE_GTK3
    sources += 'src/gtk/iupgtk_draw_cairo.c'
    sources += 'src/gtk/iupgtk_info.c'
  else
    sources += 'src/mot/iupx11_info.c'
    if USE_NEW_DRAW
      sources += 'src/gtk/iupgtk_draw_cairo.c'
    else
      sources += 'src/iupgtk_draw_gdk.c'
    endif
  endif

endif

if driver == 'WIN'
#    DEFINES += _WIN32_WINNT=$(WIN32VER) _WIN32_IE=0x600 WINVER=$(WIN32VER) NOTREEVIEW
#    SRC += win/iupwindows_main.c win/iupwindows_help.c win/iupwindows_info.c
endif

#if driver == 'GTK_MAC'
#      SRC += gtk/iupmac_help.c gtk/iupmac_info.c
#      DEFINES += GTK_MAC
#endif

#      #GDK_NULL = Yes
#      ifdef GDK_NULL 
#        #to completely remove X11 calls
#        #works only for GTK3
#        DEFINES += GDK_NULL
#      else
#        USE_X11 = Yes
#      endif

#      SRC +=  mot/iupunix_info.c
#        SRC += gtk/iupgtk_info.c
#      else
#        # Because of iupdrvGetScreenSize limitation
#        ifdef GDK_NULL 
#          SRC += gtk/iupgtk_info.c
#        else
#          SRC += mot/iupx11_info.c
#        endif
#      endif
#    endif
#  endif


if driver == 'MOTIF'
#  SRC += mot/iupmot_common.c mot/iupmot_color.c mot/iupmot_focus.c mot/iupmot_font.c \
#         mot/iupmot_key.c mot/iupmot_loop.c mot/iupmot_open.c mot/iupmot_tips.c \
#         mot/iupmot_globalattrib.c mot/iupmot_dialog.c mot/iupmot_messagedlg.c mot/iupmot_draw_x11.c \
#         mot/iupmot_timer.c mot/iupmot_image.c mot/iupmot_label.c mot/iupmot_canvas.c \
#         mot/iupmot_fontdlg.c mot/iupmot_filedlg.c mot/iupmot_frame.c \
#         mot/iupmot_button.c mot/iupmot_toggle.c mot/iupmot_progressbar.c mot/iupmot_clipboard.c \
#         mot/iupmot_text.c mot/iupmot_val.c mot/iupmot_tabs.c mot/iupmot_menu.c \
#         mot/iupmot_list.c mot/iupmot_tree.c mot/iupmot_dragdrop.c mot/iupmot_str.c \
#         mot/iupmot_calendar.c iup_datepick.c
#  SRC += mot/iupunix_help.c mot/iupunix_info.c mot/iupx11_info.c
#  USE_X11 = Yes
#  INCLUDES += mot
endif

#  SRC += win/iupwin_common.c win/iupwin_brush.c win/iupwin_focus.c win/iupwin_font.c \
#         win/iupwin_globalattrib.c win/iupwin_handle.c win/iupwin_key.c win/iupwin_str.c \
#         win/iupwin_loop.c win/iupwin_open.c win/iupwin_tips.c win/iupwin_info.c \
#         win/iupwin_dialog.c win/iupwin_messagedlg.c win/iupwin_timer.c \
#         win/iupwin_image.c win/iupwin_label.c win/iupwin_canvas.c win/iupwin_frame.c \
#         win/iupwin_fontdlg.c win/iupwin_filedlg.c win/iupwin_dragdrop.c \
#         win/iupwin_button.c win/iupwin_draw.c win/iupwin_toggle.c win/iupwin_clipboard.c \
#         win/iupwin_progressbar.c win/iupwin_text.c win/iupwin_val.c win/iupwin_touch.c \
#         win/iupwin_tabs.c win/iupwin_menu.c win/iupwin_list.c win/iupwin_tree.c \
#         win/iupwin_calendar.c win/iupwin_datepick.c
#
#  ifdef USE_NEW_DRAW
#    INCLUDES += win/wdl
#    DEFINES += COBJMACROS _UNICODE USE_NEW_DRAW
#    WDL := win/wdl/backend-d2d.c win/wdl/backend-dwrite.c win/wdl/backend-gdix.c win/wdl/backend-wic.c \
#           win/wdl/bitblt.c win/wdl/brush.c win/wdl/cachedimage.c win/wdl/canvas.c win/wdl/draw.c \
#           win/wdl/fill.c win/wdl/font.c win/wdl/image.c win/wdl/init.c win/wdl/memstream.c \
#           win/wdl/misc.c win/wdl/path.c win/wdl/string.c win/wdl/strokestyle.c
#    SRC += win/iupwin_draw_wdl.c win/iupwin_draw_gdi.c iupwin_image_wdl.c $(WDL)
#  else
#    SRC += win/iupwin_draw_gdi.c
#  endif
#  SRC += win/iupwindows_main.c win/iupwindows_help.c win/iupwindows_info.c
#  INCLUDES += win
#  DEFINES += _WIN32_WINNT=$(WIN32VER) _WIN32_IE=0x600 WINVER=$(WIN32VER) NOTREEVIEW
#  DEFINES += UNICODE
#endif
#endif
#endif

iup = static_library('iup', sources,
        include_directories: [ inc_dir ],
        dependencies: dependencies,
    )
iup_dep = declare_dependency(
        link_with : iup,
        include_directories : inc_dir,
    )

###
### Examples
###

executable('example2_1', 'example/example2_1.c',
        dependencies: [ iup_dep ],
    )

executable('example2_2', 'example/example2_2.c',
        dependencies: [ iup_dep ],
    )

executable('example2_3', 'example/example2_3.c',
        dependencies: [ iup_dep ],
    )

executable('example2_4', 'example/example2_4.c',
        dependencies: [ iup_dep ],
    )

executable('example2_5', 'example/example2_5.c',
        dependencies: [ iup_dep ],
    )
