{
	'includes': [
		 '../../common.gypi',
	],
	'targets': [
	{
		'target_name': 'mcfcore',
		'type': 'shared_library',
		'defines' : [
			'NEED_STRDUP',
			'NEED_MEMCCPY',
		],
		'dependencies' : [
			'<(third_party_dir)/libs.gyp:curl_lib',
			'<(static_dir)/util_thread/util_thread.gyp:threads',
			'<(static_dir)/util/util.gyp:*',
			'<(static_dir)/util_fs/util_fs.gyp:util_fs',
			'<(static_dir)/umcf/umcf.gyp:umcf',
			'<(third_party_dir)/sqlite/sqlite.gyp:sqlite',
			'<(third_party_dir)/sqlite3x/sqlite3x.gyp:sqlite3x',
			'<(third_party_dir)/tinyxml/tinyxml.gyp:tinyxml',
			'<(third_party_dir)/libs.gyp:curl',
			'<(third_party_dir)/libs.gyp:boost',
		],
		'ldflags': [
			'-lboost_date_time-desura',
		],
		'include_dirs': [
			'./code',
			'./RES',
			'<(third_party_dir)/courgette/include',
		],
		'sources': [
			'./code/Log.cpp',
			'./code/Courgette.cpp',
			'./code/MCFDPReporter.cpp',
			'./code/MCFMain.cpp',
			'./code/ProgressiveCRC.cpp',
			'./code/ProviderManager.cpp',
			'./code/XMLSaveAndCompress.cpp',
			'./code/mcf/MCF.cpp',
			'./code/mcf/MCFFile.cpp',
			'./code/mcf/MCFHeader.cpp',
			'./code/mcf/MCF_Http.cpp',
			'./code/mcf/MCF_Patch.cpp',
			'./code/mcf/MCF_Save.cpp',
			'./code/thread/BaseMCFThread.cpp',
			'./code/thread/HGTController.cpp',
			'./code/thread/MCFServerCon.cpp',
			'./code/thread/SFTController.cpp',
			'./code/thread/SFTWorker.cpp',
			'./code/thread/SMTController.cpp',
			'./code/thread/SMTWorker.cpp',
			'./code/thread/UpdateThread.cpp',
			'./code/thread/WGTController.cpp',
			'./code/thread/WGTWorker.cpp',
		],
	}],
}
