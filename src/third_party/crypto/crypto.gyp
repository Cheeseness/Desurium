{
	'includes' : [
		'../../common.gypi',
	],
	'targets': [
	{
		'target_name': 'crypto',
		'type': 'static_library',
		'include_dirs': [
			'./code',
			'./include',			
		],
		'all_dependent_settings': {
			'include_dirs': [
				'./include',
			],
		},
		'cflags' : [
			'-fPIC',
		],
		'sources': [
			'code/3way.cpp',
			'code/adler32.cpp',
			'code/algebra.cpp',
			'code/algparam.cpp',
			'code/arc4.cpp',
			'code/asn.cpp',
			'code/authenc.cpp',
			'code/base32.cpp',
			'code/base64.cpp',
			'code/basecode.cpp',
			'code/bench.cpp',
			'code/bench2.cpp',
			'code/bfinit.cpp',
			'code/blowfish.cpp',
			'code/blumshub.cpp',
			'code/camellia.cpp',
			'code/cast.cpp',
			'code/casts.cpp',
			'code/cbcmac.cpp',
			'code/ccm.cpp',
			'code/channels.cpp',
			'code/cmac.cpp',
			'code/cpu.cpp',
			'code/crc.cpp',
			'code/cryptlib.cpp',
			'code/cryptlib_bds.cpp',
			'code/datatest.cpp',
			'code/default.cpp',
			'code/des.cpp',
			'code/dessp.cpp',
			'code/dh.cpp',
			'code/dh2.cpp',
			'code/dsa.cpp',
			'code/eax.cpp',
			'code/ec2n.cpp',
			'code/eccrypto.cpp',
			'code/ecp.cpp',
			'code/elgamal.cpp',
			'code/emsa2.cpp',
			'code/eprecomp.cpp',
			'code/esign.cpp',
			'code/files.cpp',
			'code/filters.cpp',
			'code/fips140.cpp',
			'code/fipsalgt.cpp',
			'code/fipstest.cpp',
			'code/gcm.cpp',
			'code/gf256.cpp',
			'code/gf2n.cpp',
			'code/gf2_32.cpp',
			'code/gfpcrypt.cpp',
			'code/gost.cpp',
			'code/gzip.cpp',
			'code/hex.cpp',
			'code/hmac.cpp',
			'code/hrtimer.cpp',
			'code/ida.cpp',
			'code/idea.cpp',
			'code/integer.cpp',
			'code/iterhash.cpp',
			'code/luc.cpp',
			'code/mars.cpp',
			'code/marss.cpp',
			'code/md2.cpp',
			'code/md4.cpp',
			'code/md5.cpp',
			'code/misc.cpp',
			'code/modes.cpp',
			'code/mqueue.cpp',
			'code/mqv.cpp',
			'code/nbtheory.cpp',
			'code/network.cpp',
			'code/oaep.cpp',
			'code/osrng.cpp',
			'code/panama.cpp',
			'code/pch.cpp',
			'code/pkcspad.cpp',
			'code/polynomi.cpp',
			'code/pssr.cpp',
			'code/pubkey.cpp',
			'code/queue.cpp',
			'code/rabin.cpp',
			'code/randpool.cpp',
			'code/rc2.cpp',
			'code/rc5.cpp',
			'code/rc6.cpp',
			'code/rdtables.cpp',
			'code/regtest.cpp',
			'code/rijndael.cpp',
			'code/ripemd.cpp',
			'code/rng.cpp',
			'code/rsa.cpp',
			'code/rw.cpp',
			'code/safer.cpp',
			'code/salsa.cpp',
			'code/seal.cpp',
			'code/seed.cpp',
			'code/serpent.cpp',
			'code/sha.cpp',
			'code/shacal2.cpp',
			'code/shark.cpp',
			'code/sharkbox.cpp',
			'code/simple.cpp',
			'code/skipjack.cpp',
			'code/socketft.cpp',
			'code/sosemanuk.cpp',
			'code/square.cpp',
			'code/squaretb.cpp',
			'code/strciphr.cpp',
			'code/tea.cpp',
			'code/test.cpp',
			'code/tftables.cpp',
			'code/tiger.cpp',
			'code/tigertab.cpp',
			'code/trdlocal.cpp',
			'code/ttmac.cpp',
			'code/twofish.cpp',
			'code/validat1.cpp',
			'code/validat2.cpp',
			'code/validat3.cpp',
			'code/vmac.cpp',
			'code/wait.cpp',
			'code/wake.cpp',
			'code/whrlpool.cpp',
			'code/winpipes.cpp',
			'code/xtr.cpp',
			'code/xtrcrypt.cpp',
			'code/zdeflate.cpp',
			'code/zinflate.cpp',
			'code/zlib.cpp',
		],
	}],
}
