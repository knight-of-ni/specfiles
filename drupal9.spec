# IMPORTANT
# This is simplified drupal9 specfile, which does not use php composer or symfony as they are not available in all epel repos
# Portions of this specfile borrowed from the Drupal 8 specfile written by Shawn Iwinski <shawn@iwin.ski>

# Build using "--with tests" to enable tests
%global with_tests 0%{?_with_tests:1}

# drupal 9 requires php 7.3 or newer
%global php_min_ver 7.3.0

# Disable automatic requires/provides processing
AutoReqProv: no

Name:      drupal9
Version:   9.1.3
Release:   1%{?dist}
Summary:   An open source content management platform
License:   GPLv2+
URL:       https://www.drupal.org/9
Source0:   http://ftp.drupal.org/files/projects/drupal-%{version}.tar.gz
Source1:   %{name}-prep-licenses-and-docs.sh

BuildArch: noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  sed
BuildRequires:  grep
BuildRequires:  php-cli

# A basic set of runtime requirements which may not be complete
Requires:  php-cli
Requires:  php(language) >= %{php_min_ver}
Requires:  php-fpm
Requires:  php-gd
Requires:  php-mysqlnd
Requires:  php-mbstring
Requires:  php-json
Requires:  php-common
Requires:  php-dba
Requires:  php-dbg
Requires:  php-embedded
Requires:  php-enchant
Requires:  php-bcmath
Requires:  php-gmp
Requires:  php-intl
Requires:  php-ldap
Requires:  php-odbc
Requires:  php-pdo
Requires:  php-opcache
Requires:  php-pear
Requires:  php-pgsql
Requires:  php-process
Requires:  php-recode
Requires:  php-snmp
Requires:  php-soap
Requires:  php-xml
Requires:  php-xmlrpc
Requires:  php-date
Requires:  php-dom
Requires:  php-filter
Requires:  php-hash
Requires:  php-pcre
Requires:  php-session
Requires:  php-simplexml
Requires:  php-spl
Requires:  php-tokenizer
Requires:  php-ctype
Requires:  php-curl
Requires:  php-ftp
Requires:  php-iconv
Requires:  php-libxml
Requires:  php-pdo_sqlite
Requires:  php-posix
Requires:  php-reflection
Requires:  php-zip
Requires:  php-zlib

# Weak dependencies
Suggests:  php-pecl(apcu)
Suggests:  php-pecl(yaml)

## Core
Provides:  drupal9(core) = %{version}
## Other
Provides:  drupal9(aaa_update_test) = %{version}
Provides:  drupal9(accept_header_routing_test) = %{version}
Provides:  drupal9(action_bulk_test) = %{version}
Provides:  drupal9(action_test) = %{version}
Provides:  drupal9(action) = %{version}
Provides:  drupal9(aggregator_display_configurable_test) = %{version}
Provides:  drupal9(aggregator_test) = %{version}
Provides:  drupal9(aggregator_test_views) = %{version}
Provides:  drupal9(aggregator) = %{version}
Provides:  drupal9(ajax_forms_test) = %{version}
Provides:  drupal9(ajax_test) = %{version}
Provides:  drupal9(automated_cron) = %{version}
Provides:  drupal9(ban) = %{version}
Provides:  drupal9(bartik) = %{version}
Provides:  drupal9(basic_auth_test) = %{version}
Provides:  drupal9(basic_auth) = %{version}
Provides:  drupal9(batch_test) = %{version}
Provides:  drupal9(bbb_update_test) = %{version}
Provides:  drupal9(big_pipe_regression_test) = %{version}
Provides:  drupal9(big_pipe_test_theme) = %{version}
Provides:  drupal9(big_pipe_test) = %{version}
Provides:  drupal9(big_pipe) = %{version}
Provides:  drupal9(block_content_test) = %{version}
Provides:  drupal9(block_content_test_views) = %{version}
Provides:  drupal9(block_content) = %{version}
Provides:  drupal9(block_test_specialchars_theme) = %{version}
Provides:  drupal9(block_test_theme) = %{version}
Provides:  drupal9(block_test) = %{version}
Provides:  drupal9(block_test_views) = %{version}
Provides:  drupal9(block) = %{version}
Provides:  drupal9(book_breadcrumb_test) = %{version}
Provides:  drupal9(book_test) = %{version}
Provides:  drupal9(book_test_views) = %{version}
Provides:  drupal9(book) = %{version}
Provides:  drupal9(breakpoint_module_test) = %{version}
Provides:  drupal9(breakpoint_theme_test) = %{version}
Provides:  drupal9(breakpoint) = %{version}
Provides:  drupal9(cache_test) = %{version}
Provides:  drupal9(ccc_update_test) = %{version}
Provides:  drupal9(ckeditor_test) = %{version}
Provides:  drupal9(ckeditor) = %{version}
Provides:  drupal9(claro) = %{version}
Provides:  drupal9(color_test_theme) = %{version}
Provides:  drupal9(color_test) = %{version}
Provides:  drupal9(color) = %{version}
Provides:  drupal9(comment_base_field_test) = %{version}
Provides:  drupal9(comment_empty_title_test) = %{version}
Provides:  drupal9(comment_test) = %{version}
Provides:  drupal9(comment_test_views) = %{version}
Provides:  drupal9(comment) = %{version}
Provides:  drupal9(common_test_cron_helper) = %{version}
Provides:  drupal9(common_test) = %{version}
Provides:  drupal9(condition_test) = %{version}
Provides:  drupal9(config_clash_test_theme) = %{version}
Provides:  drupal9(config_collection_clash_install_test) = %{version}
Provides:  drupal9(config_collection_install_test) = %{version}
Provides:  drupal9(config_entity_static_cache_test) = %{version}
Provides:  drupal9(config_events_test) = %{version}
Provides:  drupal9(config_exclude_test) = %{version}
Provides:  drupal9(config_import_test) = %{version}
Provides:  drupal9(config_install_dependency_test) = %{version}
Provides:  drupal9(config_install_double_dependency_test) = %{version}
Provides:  drupal9(config_install_fail_test) = %{version}
Provides:  drupal9(config_integration_test) = %{version}
Provides:  drupal9(config_other_module_config_test) = %{version}
Provides:  drupal9(config_override_integration_test) = %{version}
Provides:  drupal9(config_override_test) = %{version}
Provides:  drupal9(config_test_id_mismatch) = %{version}
Provides:  drupal9(config_test_language) = %{version}
Provides:  drupal9(config_test_rest) = %{version}
Provides:  drupal9(config_test) = %{version}
Provides:  drupal9(config_transformer_test) = %{version}
Provides:  drupal9(config_translation_test_theme) = %{version}
Provides:  drupal9(config_translation_test) = %{version}
Provides:  drupal9(config_translation) = %{version}
Provides:  drupal9(config) = %{version}
Provides:  drupal9(conneg_test) = %{version}
Provides:  drupal9(contact_storage_test) = %{version}
Provides:  drupal9(contact_test) = %{version}
Provides:  drupal9(contact_test_views) = %{version}
Provides:  drupal9(contact) = %{version}
Provides:  drupal9(content_moderation_test_local_task) = %{version}
Provides:  drupal9(content_moderation_test_views) = %{version}
Provides:  drupal9(content_moderation) = %{version}
Provides:  drupal9(content_translation_test) = %{version}
Provides:  drupal9(content_translation_test_views) = %{version}
Provides:  drupal9(content_translation) = %{version}
Provides:  drupal9(contextual_test) = %{version}
Provides:  drupal9(contextual) = %{version}
Provides:  drupal9(cron_queue_test) = %{version}
Provides:  drupal9(csrf_race_test) = %{version}
Provides:  drupal9(csrf_test) = %{version}
Provides:  drupal9(css_disable_transitions_test) = %{version}
Provides:  drupal9(database_statement_monitoring_test) = %{version}
Provides:  drupal9(database_test) = %{version}
Provides:  drupal9(datetime_range_test) = %{version}
Provides:  drupal9(datetime_range) = %{version}
Provides:  drupal9(datetime_test) = %{version}
Provides:  drupal9(datetime) = %{version}
Provides:  drupal9(dblog_test_views) = %{version}
Provides:  drupal9(dblog) = %{version}
Provides:  drupal9(default_format_test) = %{version}
Provides:  drupal9(delay_cache_tags_invalidation) = %{version}
Provides:  drupal9(demo_umami) = %{version}
Provides:  drupal9(deprecation_test) = %{version}
Provides:  drupal9(dialog_renderer_test) = %{version}
Provides:  drupal9(display_variant_test) = %{version}
Provides:  drupal9(driver_test) = %{version}
Provides:  drupal9(drupal_system_cross_profile_test) = %{version}
Provides:  drupal9(drupal_system_listing_compatible_test) = %{version}
Provides:  drupal9(dynamic_page_cache_test) = %{version}
Provides:  drupal9(dynamic_page_cache) = %{version}
Provides:  drupal9(early_rendering_controller_test) = %{version}
Provides:  drupal9(early_translation_test) = %{version}
Provides:  drupal9(editor_private_test) = %{version}
Provides:  drupal9(editor_test) = %{version}
Provides:  drupal9(editor) = %{version}
Provides:  drupal9(element_info_test) = %{version}
Provides:  drupal9(entity_crud_hook_test) = %{version}
Provides:  drupal9(entity_reference_test) = %{version}
Provides:  drupal9(entity_reference_test_views) = %{version}
Provides:  drupal9(entity_schema_test) = %{version}
Provides:  drupal9(entity_serialization_test) = %{version}
Provides:  drupal9(entity_test_constraints) = %{version}
Provides:  drupal9(entity_test_extra) = %{version}
Provides:  drupal9(entity_test_operation) = %{version}
Provides:  drupal9(entity_test_revlog) = %{version}
Provides:  drupal9(entity_test_schema_converter) = %{version}
Provides:  drupal9(entity_test_third_party) = %{version}
Provides:  drupal9(entity_test_update) = %{version}
Provides:  drupal9(entity_test) = %{version}
Provides:  drupal9(error_service_test) = %{version}
Provides:  drupal9(error_test) = %{version}
Provides:  drupal9(experimental_module_dependency_test) = %{version}
Provides:  drupal9(experimental_module_requirements_test) = %{version}
Provides:  drupal9(experimental_module_test) = %{version}
Provides:  drupal9(experimental_theme_dependency_test) = %{version}
Provides:  drupal9(experimental_theme_test) = %{version}
Provides:  drupal9(field_discovery_test) = %{version}
Provides:  drupal9(field_layout_test) = %{version}
Provides:  drupal9(field_layout) = %{version}
Provides:  drupal9(field_normalization_test) = %{version}
Provides:  drupal9(field_plugins_test) = %{version}
Provides:  drupal9(field_test_boolean_access_denied) = %{version}
Provides:  drupal9(field_test_config) = %{version}
Provides:  drupal9(field_test) = %{version}
Provides:  drupal9(field_test_views) = %{version}
Provides:  drupal9(field_third_party_test) = %{version}
Provides:  drupal9(field_timestamp_test) = %{version}
Provides:  drupal9(field_ui_test) = %{version}
Provides:  drupal9(field_ui) = %{version}
Provides:  drupal9(field) = %{version}
Provides:  drupal9(file_module_test) = %{version}
Provides:  drupal9(file_test) = %{version}
Provides:  drupal9(file_test_views) = %{version}
Provides:  drupal9(file) = %{version}
Provides:  drupal9(filter_test_plugin) = %{version}
Provides:  drupal9(filter_test) = %{version}
Provides:  drupal9(filter) = %{version}
Provides:  drupal9(form_test) = %{version}
Provides:  drupal9(forum_test_views) = %{version}
Provides:  drupal9(forum) = %{version}
Provides:  drupal9(hal_test) = %{version}
Provides:  drupal9(hal) = %{version}
Provides:  drupal9(help_test) = %{version}
Provides:  drupal9(help_topics_test_theme) = %{version}
Provides:  drupal9(help_topics_test) = %{version}
Provides:  drupal9(help_topics) = %{version}
Provides:  drupal9(help) = %{version}
Provides:  drupal9(history) = %{version}
Provides:  drupal9(hold_test) = %{version}
Provides:  drupal9(httpkernel_test) = %{version}
Provides:  drupal9(image_access_test_hidden) = %{version}
Provides:  drupal9(image_module_test) = %{version}
Provides:  drupal9(image_test) = %{version}
Provides:  drupal9(image_test_views) = %{version}
Provides:  drupal9(image) = %{version}
Provides:  drupal9(inline_form_errors) = %{version}
Provides:  drupal9(invalid_module_name_over_the_maximum_allowed_character_length) = %{version}
Provides:  drupal9(js_ajax_test) = %{version}
Provides:  drupal9(js_cookie_test) = %{version}
Provides:  drupal9(js_deprecation_log_test) = %{version}
Provides:  drupal9(js_deprecation_test) = %{version}
Provides:  drupal9(js_message_test) = %{version}
Provides:  drupal9(jsonapi_test_collection_count) = %{version}
Provides:  drupal9(jsonapi_test_data_type) = %{version}
Provides:  drupal9(jsonapi_test_field_access) = %{version}
Provides:  drupal9(jsonapi_test_field_aliasing) = %{version}
Provides:  drupal9(jsonapi_test_field_filter_access) = %{version}
Provides:  drupal9(jsonapi_test_field_type) = %{version}
Provides:  drupal9(jsonapi_test_normalizers_kernel) = %{version}
Provides:  drupal9(jsonapi_test_resource_type_building) = %{version}
Provides:  drupal9(jsonapi_test_user) = %{version}
Provides:  drupal9(jsonapi) = %{version}
Provides:  drupal9(js_webassert_test) = %{version}
Provides:  drupal9(language_config_override_test) = %{version}
Provides:  drupal9(language_elements_test) = %{version}
Provides:  drupal9(language_entity_field_access_test) = %{version}
Provides:  drupal9(language_test) = %{version}
Provides:  drupal9(language) = %{version}
Provides:  drupal9(layout_builder_defaults_test) = %{version}
Provides:  drupal9(layout_builder_fieldblock_test) = %{version}
Provides:  drupal9(layout_builder_form_block_test) = %{version}
Provides:  drupal9(layout_builder_overrides_test) = %{version}
Provides:  drupal9(layout_builder_test) = %{version}
Provides:  drupal9(layout_builder_theme_suggestions_test) = %{version}
Provides:  drupal9(layout_builder) = %{version}
Provides:  drupal9(layout_builder_views_test) = %{version}
Provides:  drupal9(layout_discovery) = %{version}
Provides:  drupal9(layout_test) = %{version}
Provides:  drupal9(lazy_route_provider_install_test) = %{version}
Provides:  drupal9(link_generation_test) = %{version}
Provides:  drupal9(link_test_views) = %{version}
Provides:  drupal9(link) = %{version}
Provides:  drupal9(locale) = %{version}
Provides:  drupal9(mail_cancel_test) = %{version}
Provides:  drupal9(mail_html_test) = %{version}
Provides:  drupal9(media_library_form_overwrite_test) = %{version}
Provides:  drupal9(media_library_test) = %{version}
Provides:  drupal9(media_library_test_widget) = %{version}
Provides:  drupal9(media_library) = %{version}
Provides:  drupal9(media_test_ckeditor) = %{version}
Provides:  drupal9(media_test_filter) = %{version}
Provides:  drupal9(media_test_oembed) = %{version}
Provides:  drupal9(media_test_source) = %{version}
Provides:  drupal9(media_test_type) = %{version}
Provides:  drupal9(media_test_views) = %{version}
Provides:  drupal9(media) = %{version}
Provides:  drupal9(menu_link_content) = %{version}
Provides:  drupal9(menu_test) = %{version}
Provides:  drupal9(menu_ui) = %{version}
Provides:  drupal9(migrate_cckfield_plugin_manager_test) = %{version}
Provides:  drupal9(migrate_drupal_ui) = %{version}
Provides:  drupal9(migrate_drupal) = %{version}
Provides:  drupal9(migrate_entity_test) = %{version}
Provides:  drupal9(migrate_events_test) = %{version}
Provides:  drupal9(migrate_external_translated_test) = %{version}
Provides:  drupal9(migrate_field_plugin_manager_test) = %{version}
Provides:  drupal9(migrate_high_water_test) = %{version}
Provides:  drupal9(migrate_lookup_test) = %{version}
Provides:  drupal9(migrate_no_migrate_drupal_test) = %{version}
Provides:  drupal9(migrate_overwrite_test) = %{version}
Provides:  drupal9(migrate_prepare_row_test) = %{version}
Provides:  drupal9(migrate_query_batch_test) = %{version}
Provides:  drupal9(migrate_state_finished_test) = %{version}
Provides:  drupal9(migrate_state_no_file_test) = %{version}
Provides:  drupal9(migrate_state_not_finished_test) = %{version}
Provides:  drupal9(migrate_state_no_upgrade_path) = %{version}
Provides:  drupal9(migrate_stub_test) = %{version}
Provides:  drupal9(migrate_track_changes_test) = %{version}
Provides:  drupal9(migrate) = %{version}
Provides:  drupal9(migration_directory_test) = %{version}
Provides:  drupal9(migration_provider_test) = %{version}
Provides:  drupal9(minimal) = %{version}
Provides:  drupal9(module_autoload_test) = %{version}
Provides:  drupal9(module_handler_test_no_hook) = %{version}
Provides:  drupal9(module_handler_test) = %{version}
Provides:  drupal9(module_install_class_loader_test1) = %{version}
Provides:  drupal9(module_install_class_loader_test2) = %{version}
Provides:  drupal9(module_installer_config_test) = %{version}
Provides:  drupal9(module_required_test) = %{version}
Provides:  drupal9(module_test) = %{version}
Provides:  drupal9(new_dependency_test) = %{version}
Provides:  drupal9(new_dependency_test_with_service) = %{version}
Provides:  drupal9(node_access_test_auto_bubbling) = %{version}
Provides:  drupal9(node_access_test_empty) = %{version}
Provides:  drupal9(node_access_test_language) = %{version}
Provides:  drupal9(node_access_test) = %{version}
Provides:  drupal9(node_display_configurable_test) = %{version}
Provides:  drupal9(node_test_config) = %{version}
Provides:  drupal9(node_test_exception) = %{version}
Provides:  drupal9(node_test) = %{version}
Provides:  drupal9(node_test_views) = %{version}
Provides:  drupal9(node) = %{version}
Provides:  drupal9(nyan_cat) = %{version}
Provides:  drupal9(off_canvas_test) = %{version}
Provides:  drupal9(options_config_install_test) = %{version}
Provides:  drupal9(options_test) = %{version}
Provides:  drupal9(options_test_views) = %{version}
Provides:  drupal9(options) = %{version}
Provides:  drupal9(page_cache_form_test) = %{version}
Provides:  drupal9(page_cache) = %{version}
Provides:  drupal9(pager_test) = %{version}
Provides:  drupal9(paramconverter_test) = %{version}
Provides:  drupal9(path_alias_deprecated_test) = %{version}
Provides:  drupal9(path_deprecated_test) = %{version}
Provides:  drupal9(path_encoded_test) = %{version}
Provides:  drupal9(path) = %{version}
Provides:  drupal9(phpunit_test) = %{version}
Provides:  drupal9(plugin_test_extended) = %{version}
Provides:  drupal9(plugin_test) = %{version}
Provides:  drupal9(quickedit_test) = %{version}
Provides:  drupal9(quickedit) = %{version}
Provides:  drupal9(rdf_conflicting_namespaces) = %{version}
Provides:  drupal9(rdf_test_namespaces) = %{version}
Provides:  drupal9(rdf_test) = %{version}
Provides:  drupal9(rdf) = %{version}
Provides:  drupal9(render_array_non_html_subscriber_test) = %{version}
Provides:  drupal9(render_attached_test) = %{version}
Provides:  drupal9(render_placeholder_message_test) = %{version}
Provides:  drupal9(requirements1_test) = %{version}
Provides:  drupal9(requirements2_test) = %{version}
Provides:  drupal9(responsive_image_test_module) = %{version}
Provides:  drupal9(responsive_image) = %{version}
Provides:  drupal9(rest_test) = %{version}
Provides:  drupal9(rest_test_views) = %{version}
Provides:  drupal9(rest) = %{version}
Provides:  drupal9(router_test) = %{version}
Provides:  drupal9(search_date_query_alter) = %{version}
Provides:  drupal9(search_embedded_form) = %{version}
Provides:  drupal9(search_extra_type) = %{version}
Provides:  drupal9(search_langcode_test) = %{version}
Provides:  drupal9(search_query_alter) = %{version}
Provides:  drupal9(search) = %{version}
Provides:  drupal9(serialization_test) = %{version}
Provides:  drupal9(serialization) = %{version}
Provides:  drupal9(service_provider_test) = %{version}
Provides:  drupal9(session_exists_cache_context_test) = %{version}
Provides:  drupal9(session_test) = %{version}
Provides:  drupal9(settings_tray_override_test) = %{version}
Provides:  drupal9(settings_tray_test_css) = %{version}
Provides:  drupal9(settings_tray_test) = %{version}
Provides:  drupal9(settings_tray) = %{version}
Provides:  drupal9(seven) = %{version}
Provides:  drupal9(shortcut) = %{version}
Provides:  drupal9(simpletest_deprecation_test) = %{version}
Provides:  drupal9(simpletest) = %{version}
Provides:  drupal9(standard) = %{version}
Provides:  drupal9(stark) = %{version}
Provides:  drupal9(statistics_test_attached) = %{version}
Provides:  drupal9(statistics_test_views) = %{version}
Provides:  drupal9(statistics) = %{version}
Provides:  drupal9(syslog_test) = %{version}
Provides:  drupal9(syslog) = %{version}
Provides:  drupal9(system_core_incompatible_semver_test) = %{version}
Provides:  drupal9(system_core_semver_test) = %{version}
Provides:  drupal9(system_dependencies_test) = %{version}
Provides:  drupal9(system_incompatible_core_version_dependencies_test) = %{version}
Provides:  drupal9(system_incompatible_core_version_test_1x) = %{version}
Provides:  drupal9(system_incompatible_core_version_test) = %{version}
Provides:  drupal9(system_incompatible_module_version_dependencies_test) = %{version}
Provides:  drupal9(system_incompatible_module_version_test) = %{version}
Provides:  drupal9(system_incompatible_php_version_test) = %{version}
Provides:  drupal9(system_mail_failure_test) = %{version}
Provides:  drupal9(system_module_test) = %{version}
Provides:  drupal9(system_project_namespace_test) = %{version}
Provides:  drupal9(system_test) = %{version}
Provides:  drupal9(system) = %{version}
Provides:  drupal9(tabledrag_test) = %{version}
Provides:  drupal9(taxonomy_crud) = %{version}
Provides:  drupal9(taxonomy_term_display_configurable_test) = %{version}
Provides:  drupal9(taxonomy_term_stub_test) = %{version}
Provides:  drupal9(taxonomy_test) = %{version}
Provides:  drupal9(taxonomy_test_views) = %{version}
Provides:  drupal9(taxonomy) = %{version}
Provides:  drupal9(telephone) = %{version}
Provides:  drupal9(test_another_module_required_by_theme) = %{version}
Provides:  drupal9(test_batch_test) = %{version}
Provides:  drupal9(test_ckeditor_stylesheets_external) = %{version}
Provides:  drupal9(test_ckeditor_stylesheets_protocol_relative) = %{version}
Provides:  drupal9(test_ckeditor_stylesheets_relative) = %{version}
Provides:  drupal9(test_core_semver) = %{version}
Provides:  drupal9(test_datatype_boolean_emoji_normalizer) = %{version}
Provides:  drupal9(test_fieldtype_boolean_emoji_normalizer) = %{version}
Provides:  drupal9(test_invalid_basetheme_sub) = %{version}
Provides:  drupal9(test_invalid_basetheme) = %{version}
Provides:  drupal9(test_invalid_core_semver) = %{version}
Provides:  drupal9(test_invalid_core) = %{version}
Provides:  drupal9(test_invalid_engine) = %{version}
Provides:  drupal9(test_invalid_region) = %{version}
Provides:  drupal9(test_layout_theme) = %{version}
Provides:  drupal9(test_legacy_stylesheets_remove) = %{version}
Provides:  drupal9(test_legacy_theme) = %{version}
Provides:  drupal9(test_messages) = %{version}
Provides:  drupal9(test_module_compatible_constraint) = %{version}
Provides:  drupal9(test_module_incompatible_constraint) = %{version}
Provides:  drupal9(test_module_required_by_theme) = %{version}
Provides:  drupal9(test_module) = %{version}
Provides:  drupal9(test_page_test) = %{version}
Provides:  drupal9(test_stable) = %{version}
Provides:  drupal9(test_subseven) = %{version}
Provides:  drupal9(test_subsubtheme) = %{version}
Provides:  drupal9(test_subtheme) = %{version}
Provides:  drupal9(test_theme_depending_on_constrained_modules) = %{version}
Provides:  drupal9(test_theme_depending_on_modules) = %{version}
Provides:  drupal9(test_theme_depending_on_nonexisting_module) = %{version}
Provides:  drupal9(test_theme_having_veery_long_name_which_is_too_long) = %{version}
Provides:  drupal9(test_theme_libraries_empty) = %{version}
Provides:  drupal9(test_theme_libraries_extend) = %{version}
Provides:  drupal9(test_theme_libraries_override_with_drupal_settings) = %{version}
Provides:  drupal9(test_theme_libraries_override_with_invalid_asset) = %{version}
Provides:  drupal9(test_theme_mixed_module_dependencies) = %{version}
Provides:  drupal9(test_theme_nyan_cat_engine) = %{version}
Provides:  drupal9(test_theme_settings_features) = %{version}
Provides:  drupal9(test_theme_settings) = %{version}
Provides:  drupal9(test_theme_theme) = %{version}
Provides:  drupal9(test_theme_twig_registry_loader_subtheme) = %{version}
Provides:  drupal9(test_theme_twig_registry_loader_theme) = %{version}
Provides:  drupal9(test_theme_twig_registry_loader) = %{version}
Provides:  drupal9(test_theme) = %{version}
Provides:  drupal9(test_theme_with_a_base_theme_depending_on_modules) = %{version}
Provides:  drupal9(test_wild_west) = %{version}
Provides:  drupal9(text) = %{version}
Provides:  drupal9(theme_legacy_suggestions_test) = %{version}
Provides:  drupal9(theme_legacy_test) = %{version}
Provides:  drupal9(theme_page_test) = %{version}
Provides:  drupal9(theme_region_test) = %{version}
Provides:  drupal9(theme_suggestions_test) = %{version}
Provides:  drupal9(theme_test) = %{version}
Provides:  drupal9(token_test) = %{version}
Provides:  drupal9(toolbar_disable_user_toolbar) = %{version}
Provides:  drupal9(toolbar_test) = %{version}
Provides:  drupal9(toolbar) = %{version}
Provides:  drupal9(tour_test) = %{version}
Provides:  drupal9(tour) = %{version}
Provides:  drupal9(tracker_test_views) = %{version}
Provides:  drupal9(tracker) = %{version}
Provides:  drupal9(trusted_hosts_test) = %{version}
Provides:  drupal9(twig_extension_test) = %{version}
Provides:  drupal9(twig_loader_test) = %{version}
Provides:  drupal9(twig_namespace_a) = %{version}
Provides:  drupal9(twig_namespace_b) = %{version}
Provides:  drupal9(twig_theme_test) = %{version}
Provides:  drupal9(twig) = %{version}
Provides:  drupal9(umami) = %{version}
Provides:  drupal9(unique_field_constraint_test) = %{version}
Provides:  drupal9(update_script_test) = %{version}
Provides:  drupal9(update_test_0) = %{version}
Provides:  drupal9(update_test_1) = %{version}
Provides:  drupal9(update_test_2) = %{version}
Provides:  drupal9(update_test_3) = %{version}
Provides:  drupal9(update_test_basetheme) = %{version}
Provides:  drupal9(update_test_failing) = %{version}
Provides:  drupal9(update_test_invalid_hook) = %{version}
Provides:  drupal9(update_test_last_removed) = %{version}
Provides:  drupal9(update_test_no_preexisting) = %{version}
Provides:  drupal9(update_test_postupdate) = %{version}
Provides:  drupal9(update_test_schema) = %{version}
Provides:  drupal9(update_test_semver_update_n) = %{version}
Provides:  drupal9(update_test_subtheme) = %{version}
Provides:  drupal9(update_test) = %{version}
Provides:  drupal9(update_test_with_7x) = %{version}
Provides:  drupal9(update) = %{version}
Provides:  drupal9(url_alter_test) = %{version}
Provides:  drupal9(user_access_test) = %{version}
Provides:  drupal9(user_batch_action_test) = %{version}
Provides:  drupal9(user_custom_phpass_params_test) = %{version}
Provides:  drupal9(user_form_test) = %{version}
Provides:  drupal9(user_hooks_test) = %{version}
Provides:  drupal9(user_test_theme) = %{version}
Provides:  drupal9(user_test_views) = %{version}
Provides:  drupal9(user) = %{version}
Provides:  drupal9(views_config_entity_test) = %{version}
Provides:  drupal9(views_entity_test) = %{version}
Provides:  drupal9(views_test_cacheable_metadata_calculation) = %{version}
Provides:  drupal9(views_test_checkboxes_theme) = %{version}
Provides:  drupal9(views_test_classy_subtheme) = %{version}
Provides:  drupal9(views_test_config) = %{version}
Provides:  drupal9(views_test_data) = %{version}
Provides:  drupal9(views_test_formatter) = %{version}
Provides:  drupal9(views_test_language) = %{version}
Provides:  drupal9(views_test_modal) = %{version}
Provides:  drupal9(views_test_query_access) = %{version}
Provides:  drupal9(views_test_rss) = %{version}
Provides:  drupal9(views_test_theme) = %{version}
Provides:  drupal9(views_ui_test_field) = %{version}
Provides:  drupal9(views_ui_test) = %{version}
Provides:  drupal9(views_ui) = %{version}
Provides:  drupal9(views) = %{version}
Provides:  drupal9(vocabulary_serialization_test) = %{version}
Provides:  drupal9(workflows) = %{version}
Provides:  drupal9(workflow_third_party_settings_test) = %{version}
Provides:  drupal9(workflow_type_test) = %{version}
Provides:  drupal9(workspace_access_test) = %{version}
Provides:  drupal9(workspaces) = %{version}
Provides:  drupal9(workspace_update_test) = %{version}

# Bundled
## core/core.libraries.yml
### core/assets/vendor/backbone
###     License:  MIT
###     Upstream: https://github.com/jashkenas/backbone
Provides:  bundled(js-backbone) = 1.4.0
### core/assets/vendor/ckeditor
###     License:  GPLv2+
###     Upstream: https://github.com/ckeditor/ckeditor-dev
Provides:  bundled(ckeditor) = 4.14.1
### core/assets/vendor/classList
###     License:  Public Domain
###     Upstream: https://github.com/eligrey/classList.js
Provides:  bundled(js-classList) = 2014_12_13
### core/assets/vendor/js-cookie
###     License:  MIT
###     Upstream: https://github.com/js-cookie/js-cookie
Provides:  bundled(js-cookie) = 3.0.0-rc0
### core/assets/vendor/domready
###     License:  MIT
###     Upstream: https://github.com/ded/domready
Provides:  bundled(js-domready) = 1.0.8
### core/assets/vendor/farbtastic
###     License:  GPLv2+
###     Upstream: https://github.com/mattfarina/farbtastic
Provides:  bundled(js-farbtastic) = 1.2
### core/assets/vendor/html5shiv
###     License:  GPLv2+
###     Upstream: https://github.com/aFarkas/html5shiv
Provides:  bundled(js-html5shiv) = 3.7.3
### core/assets/vendor/jquery
###     License:  MIT
###     Upstream: https://github.com/jquery/jquery
Provides:  bundled(js-jquery) = 3.5.1
### core/assets/vendor/jquery.cookie
###     License:  MIT
###     Upstream: https://github.com/carhartl/jquery-cookie
Provides:  bundled(js-jquery-cookie) = 1.4.1
### core/assets/vendor/jquery-form
###     License:  GPLv2+
###     Upstream: https://github.com/jquery-form/form
Provides:  bundled(js-jquery-form) = 4.22
### core/assets/vendor/jquery-joyride
###     License:  MIT
###     Upstream: https://github.com/zurb/joyride
Provides:  bundled(js-jquery-joyride) = 2.1.0.1
### core/assets/vendor/jquery-once
###     License:  GPLv2+
###     Upstream: https://github.com/RobLoach/jquery-once
Provides:  bundled(js-jquery-once) = 2.2.3
### core/assets/vendor/jquery.ui
###     License:  Public Domain
###     Upstream: https://github.com/jquery/jquery-ui
Provides:  bundled(js-jquery-ui) = 1.12.1
### core/assets/vendor/jquery-ui-touch-punch
###     License:  GPLv2+
###     Upstream: https://github.com/furf/jquery-ui-touch-punch
Provides:  bundled(js-jquery-ui-touch-punch) = 0.2.3
### core/assets/vendor/matchMedia
###     License:  MIT
###     Upstream: https://github.com/paulirish/matchMedia.js
Provides:  bundled(js-matchMedia) = 0.2.0
### core/assets/vendor/modernizr
###     License:  MIT
###     Upstream: https://github.com/Modernizr/Modernizr
Provides:  bundled(js-modernizr) = 3.3.1
### core/assets/vendor/normalize-css
###     License:  MIT
###     Upstream: https://github.com/necolas/normalize.css
Provides:  bundled(css-normalize) = 3.0.3
### core/assets/vendor/picturefill
###     License:  MIT
###     Upstream: https://github.com/scottjehl/picturefill
Provides:  bundled(js-picturefill) = 3.0.3
### core/assets/vendor/popperjs
###     License: MIT
###     Upstream: https://github.com/popperjs/popper.js
Provides:  bundled(js-popperjs) = 1.16.0
### core/assets/vendor/sortable
###     License: MIT
###     Upstream: https://github.com/SortableJS/Sortable
Provides:  bundled(js-sortable) = 1.10.2
### core/assets/vendor/underscore
###     License:  MIT
###     Upstream: https://github.com/jashkenas/underscore
Provides:  bundled(js-underscore) = 1.9.1

%description
Drupal is an open source content management platform powering millions of
websites and applications. It’s built, used, and supported by an active and
diverse community of people around the world.

%prep
%autosetup -n drupal-%{version}
mkdir .rpm
cp -p %{SOURCE1} .rpm/

# Remove unneeded files
rm -rf vendor core/vendor
rm -f core/composer.json
find . -name '.git*' -delete -print
find . -name 'web.config' -delete -print

# Licenses and docs
.rpm/%{name}-prep-licenses-and-docs.sh
mv core/INSTALL.*.* .rpm/docs/core/

# Move license and doc files required at runtime back in place
mv .rpm/docs/core/modules/system/tests/fixtures/HtaccessTest/composer.* \
    core/modules/system/tests/fixtures/HtaccessTest/
rmdir .rpm/docs/core/modules/system/tests/fixtures/HtaccessTest
rmdir .rpm/docs/core/modules/system/tests/fixtures
cp .rpm/docs/core/INSTALL.txt core/

# Remove all empty license and doc files
find .rpm/{licenses,docs}/ -type f -size 0 -delete -print

# Apache .htaccess
sed 's!# RewriteBase /$!# RewriteBase /\n  RewriteBase /drupal9!' \
    -i .htaccess

# Update php bin
sed 's#/bin/php#%{_bindir}/php#' \
    -i core/scripts/update-countries.sh

# Fix "non-executable-script" rpmlint errors
chmod +x core/scripts/*.{php,sh}

# Fix "script-without-shebang" rpmlint errors
chmod -x core/scripts/run-tests.sh

%build
# nothing to build

%install
# Main
mkdir -p %{buildroot}%{_datadir}/drupal9
cp -pr * %{buildroot}%{_datadir}/drupal9/

# Sites
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/sites
mv %{buildroot}%{_datadir}/drupal9/sites/* %{buildroot}%{_sysconfdir}/%{name}/sites/
rmdir %{buildroot}%{_datadir}/drupal9/sites
ln -s %{_sysconfdir}/%{name}/sites %{buildroot}%{_datadir}/drupal9/sites

# Files
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}/files/{public,private}/default
ln -s %{_localstatedir}/lib/%{name}/files/public/default \
    %{buildroot}%{_sysconfdir}/%{name}/sites/default/files

# Robots
mv %{buildroot}%{_datadir}/drupal9/robots.txt %{buildroot}%{_sysconfdir}/%{name}/
ln -s %{_sysconfdir}/%{name}/robots.txt %{buildroot}%{_datadir}/drupal9/robots.txt

%check
# Version check
%{_bindir}/php -r '
    require_once "%{buildroot}%{_datadir}/drupal9/core/lib/Drupal.php";
    $version = \Drupal::VERSION;
    echo "Version $version (expected %{version})\n";
    exit(version_compare("%{version}", "$version", "=") ? 0 : 1);
'

# Ensure php bin updated
! grep -r '#!/bin/php' .

%if %{with_tests}
pushd core
    # Unit tests
    %{_bindir}/phpunit
popd
%else
# Test suite skipped
%endif

%files
%license .rpm/licenses/*
%doc .rpm/docs/*
%config(noreplace) %{_sysconfdir}/%{name}/robots.txt
%ghost %{_datadir}/drupal9/sites/default/settings.php

%{_datadir}/drupal9/
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/sites
%config(noreplace) %{_sysconfdir}/%{name}/sites/development.services.yml
%dir %{_sysconfdir}/%{name}/sites/default
## Managed upstream example/default configs
%config %{_sysconfdir}/%{name}/sites/example.*
%config %{_sysconfdir}/%{name}/sites/default/default.*
# Files
%{_sysconfdir}/%{name}/sites/default/files
%dir %{_localstatedir}/lib/%{name}
%dir %{_localstatedir}/lib/%{name}/files
%dir %{_localstatedir}/lib/%{name}/files/private
%dir %{_localstatedir}/lib/%{name}/files/public

%changelog
* Sat Jan 30 2021 Andrew Bauer <zonexpertconsulting@outlook.com> - 9.1.3-1
- Initial specfile for drupal 9

