from assets import asset

def application(environ, start_response):
##    print('\n'.join([str(('%s: %s' % (key, value)).encode('utf-8'))
##                     for key, value in environ.items()]))

    host = environ['HTTP_HOST']

    if host == 'theaterdays-zh.appspot.com' or \
       host == 'theaterdays-ko.appspot.com':
        status = '200 OK'
        headers = [('Content-Type', 'application/json'),
                   ('Vary', 'Accept-Encoding'),
                   ('X-Appengine-Log-Flush-Count', '1'),
                   ('X-Asset-Version', '120000'),
                   ('X-Encryption', 'on'),
                   ('X-Encryption-Compress', 'gzip'),
                   ('X-Encryption-Mode', '3'),
                   ('X-Force-Update-Date', '2021-09-27T04:00:00+0000'),
                   ('X-Require-Client-Version', '2.1.000'),
                   #('X-Server-Date', '2022-01-28T03:56:29+0000'),
                   ('X-Server-Date', '2022-02-01T20:00:00+0000'),
                   ('X-Cloud-Trace-Context', 'feebbe68ee9fbaaeedaa3e6c996c7681;o=1'),
                   #('Date', 'Mon, 28 Jan 2022 03:56:29 GMT'),
                   #('Date', 'Mon, 31 Jan 2022 21:00:00 GMT'),
                   ('Cache-Control', 'private'),
                   ('Alt-Svc', 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"')]
        start_response(status, headers)

        service = environ['PATH_INFO'].split('/')[-1]
        if service == 'GrecoService.AppBoot':
            return [b'1NzbIJMBO_44UDat84Ie6oj5Jzerxa3FmgLJTqKXhN-cFv85EFdXagBscxpZvtUGmu-0o5eOVi4XORUN-TvuiRPaB3oETdIO_giVfCmyfQs=']
        elif service == 'GameService.GetVersion':
            return [b'ECFgxyPGblwZo_xdafSu2O24jrHiJY9IJURP846gpKmbM2_wk4N5Kq9J3zra66aybkLKUmSEWHw8Dv0kaB-rzBALPwElXSWEJT01IpzUX0I4h63EAenFpl7ay8NTDTqP3EtCZS0dy-5DzeiYZ9SpXxgVtIH6W6rO6FP3mFL0kg6H-2syULm-tpEqzm3LGNyV6qWGQ8uSQM-mq0boc0vWEZSprkOTD46Zi-kEd_VDHUkr9wzA29U3RDw-ZlC_wPz1THdLLC-IehKwmuunvvaY-prlHTAe2JWstJNEWgKMLoZ9lgOPGVtybs45AGFNZlk0Xa_BnKR96ITcrWLy9j5qsdlrBwRFdkXlR4Lx4t-m5xonNnkE-jtDeggUqpSIq9xia3j2TtwAmF8_Ouxtj13cEDQJJ-upo27txdWQk_2rKyKD5bYCLB6SKL0MUSZzW0MD3NllssvoNG4wsghTIi-IAhMc0oZmkteTACJJ3y33zRCh6UC-CNeVm8OKVOt_M4-TDVORXhtNv_KTA2bd3yN2jmWGNimEfOpuNlyddUPC_fAgZx1uDsCpUSGA85f0TdeuwDB-JhA6zttbCzqC1wec4ovn9NUd9KUbDsVRaPwDgRo=']
        elif service == 'AuthService.Login':
            return [b'DItruvLu2vCce0NGUToZ6dE9FuhKg-bObpQE59d_Njc_qC_6VvbHxJ4oE-INzJ9RRE8KZthd39ZTeXE5YVcNJCzz7qElInB85l6Ye-qoIssbTHmiYv0c_rsNbM0KEaq4UNuyKJcqJQ4BhGiBYnx1Igld-p63CcEOfEH6xgsfCg0hrU7eD43iLy-eECUcrCzZzQdyYogrr5z0wxkkBVi0ZEMsAHI8t3xAr54PyTo0NJB_7pZ1UEEMlbnBK04dqiqw7B-tSzytBb5tmmwPzNvoo1hffdgI6kyusiPtUeJmkUbNwJcVQHEb4P2J9LIJBmnDqteT-V1ua4dnpLVrgimdTgUmbt63E9PKdHkfGzff6uCUbcFLjkq41QtHLfPKfyJURg48zVxjlBcMJfYH-NCydjjJ7Hs-0Ft5Y4XCg3B7s7MQT6yk0CrLz2NfPXJsqK2ZM39E7nbLQ6g_2ZIoXAkcPV7Yd3DRxLof2zwNdKnslAxJBEdIe-ky_URCAeqaMLNLi9hVdw__jn4CeJotrt2nSSZj79fVVEnLDOMTzlv7nftC5evhSjquLAItXNYr2g9IcFJBZWN1gULQQsdjFm_iQm_1ueoxA2tLfdX1ODPOy_i7BOkFSOZ_AmKVgZX-bEEuZuEKxa36xkcfXsXmTog_dRhPzEqqa0s4BrQMMSfOtq31-SZ7CGbwV3hIXa5ydNQub1JNYfUVQRT7yNKfiLoKyH47PuiCKEktXqMlt2H5zAV2CAQyXaBMeLRAesSTS-v4rqfcZH5WVe4lNhJ3KPoB6TGmmDSQkIi9konAXcmAiUgPXiPEBeQXxraN0CLSBPyTVlehyiOFZsk9HTzLMRqDWqyZnky3L2mTs3-9xxFBhZf9negGOoFwGTXcSjoKQDXqMqwqq6fhP3rnLb7PWePMEhfB791ZqwzBwaPsV8COU-_ZThfaMXlZnAEav9pcdrecvLITbfCuqx6_Xouyjt7jcBrUDZo-zUxO5mebFNAL7OnbZp_YPq9RqizXmjZOrmExbK31S_OqejcIYYwf630R7clafIFBm2OnvBN_sUY-7vD6r80EHndhVREkh-KQ8RHFKUNh63uTdL227NBs0uzUlRa4Qf4Q2KDf4OfGecGaSOqh36zcYsu1h3GCGxutHkf09g7whRG_noMvfP3NfY0RRkvs2YQ-RIT5GoaIwyha1pZ0grdrI_ZONBkEDyllafVhJuimwhu90gtnJEislkKseRC716xlaipbQCjLQmlqOoKbwMfiBBG5BTe9EyZbCI8lH1es7vDfeEqeKpYktYmG6T3oVTpttseBY9szGSTa463Bi4y91tyKVCvlstXzlaeYeGvdrCZGQgodnb6co7aXQ5AnJXgkehARKJEX2TrlQ-LwCU8Dxswmb3ddqRDrKcA0qf3xlEMACS_Fo-JqZXywbtkgy7ZFVubU9GYVAsYvd8mFOyGxPI0mb_FX66ybiYe8pp5JUDlme-REASGhYd7IitDDnv4ZOPfQjKKywal_OAYhLi1zJImm7r7QuqBAqoTwMrOCJiBton7HI4JlHoKfnATv4MsRR6AMT3ZSQtynmEPapqDutZI9RBhXDfEibQLxXzZGHcmAnpKyAolMYDmMVfLgyZheEnvb0IJrnQrP3_aEvfWuu3T2Vl7Lp0XQTdfV2W3SKdVPyRt3z-2rgP2Hak75mIJe2j4Vcd8qCgJy365JwQRSC9_3ZP6KvMccO7Bs27tSllKIebSqoxQUs_H4HNuD4GPdw_WO-dqHstXAWYUYWxj08TwQn0obiytI1h3Sn963tjqeFqxvCxkppTGE6RY1f3VV0GDyLGxkyOTLrfWarA4s6E7LPXGxqH57nzrrhAOO3qj3QNCE5hEE_SUVMJcz4b1ypvCstJAJ1v6-iggnjFOsKGK0-aQYIhPlqj2XbI8Bi4Jtw4uCN-UytHGDAHTXejzVb5iwPo2v4ygzKjRJTzVe6YMXHH-FCMwR4AZcXO6SE9EN2H_zlWzUd1Hm114cVhKeXNY_voLPfeMGcFYey-8PdR6V_CG_BB2SVxXaypdVPyRUcmh6smkm3Y4ParuJwDQ8QWgzNheIfBd9qFce2y0k_3mkzn1Ha44qQbb6W5PR6b3wRl_tcoyjNvbD-x3Vwv6tCVQAl8TRGzCM50BRTsdvnGTYHzNvCxR-XZADplvKr-28EiN8XZrKiYFgI1t64KCiO_Qif-Up3z0JSOWMfzaOxLiacXzUj8Aits-oH4zQ59u-PwY83oPjn4EZhrhmjEeRewFrHPWUHr5_Bo3AJ01ladws5wYP61Siq6OY5EoTfzFFQurqBR22lYyXuZ5wKBGBBM17cKxXacNXRUZml8PEjOg0jQJBYKNUaFFuyj4sYwUH9Ih36Zzzn8hp21AKpt1I2qxg_Z4yR6hV3gzPyqPfa17G_zkImeq0MZLEPZl1V5DVFqEVU5waRBYxMJZY0sTto1E2hGqC41wggH9uQqtkOWCrpx9cDO_WRhFdC_ogmjNYxkdGHSHdqbbDZAMoaxi7loYKZ7x1xQtv8nvDF8uhcpJs00KET19MXidyuLc7hXlyTdsXhNdE5eou90PmGIZwvI7b5fv1EiV-0S88Hk7bTZiOScZvd_IjsvNC7eGIwlIcnqmIwVgakkJTQr-X2ITLf9Z_at1fzDeUyLgQztmCps8MXc9lQyK_zjC_F0vKsNOIGdambI55xYtLyUnkoE8iJtN6VR7wZlz0zgZuIEMCa-fTeu1UFBOmy29u8AvMT4NVs6u7tLVSG6B2_QLtaSOytuQbQcxmGlhg6bZscvKiv0FGuam3L-CDMMRFHtIwFz9nRLYKHElccbWliqj9vI6WxZE7aEm7r--ubyyuCjyjcnPSJUBKAwnGuQTRHG-qIOI9IZUvd_-oGkY00QK8EP3hQ2-X5-Hz6dOZbemUQNvpuZfkBt-ujMBFERoPFxXapxALqZ424EpfEisrTrPqGXBqK_zJy2JXYoKXUepe_TMo2OMIpuwj71kJzcMI4KEZMFtLEExtHIcJ5LLIi2HNfxd-I3Y6HQJiEbyJ4XAJADFw8MuOyjTPQeDb1dAwa5D2Kr0ZIfcRTFpm_qisOqcK3oRUq8CW2yPzptB23vKgYFb4Nwp1oEzZc2ak_QgugXGWQN4RIISljNJmDMloepxbP-awoKNV7GceLtg7a6NM-srHiJybBN4n_5qVWF9UH_oava_9pC1pl7icSgrMx13nsnh8e3mbt0cgbSsyjvy7aTLrtNBNRnLzJjfSiAn68EUOUiQj0mM7FFKWrTDwVk8hNlBCOZEIcSZiyObFqgeOlw0E8Mui0PEGDjRdc9EAU3ukzM3iD_lsZORhvTC6Kr3ITfvHPHUNLA1BxPkHkb61IjlBgXFKLAEKhF1PXAnPMik_S1HQF9A9T1AXDG9rCEnLcHg_iH9cOf4hw2lDn9kx4ZeGRU_Ph6rS8iRYnvTYVpLRv9kRmnYt_c6lJvJ2ydyCRyZ-31pT2A945SrAbGqoKzzbRdNBhvukod8WPHpezUlwibnLQOZc6UVdFfNZFaz2aWN36LAlMWime62SSUBdh6OlYkBl0RO6xiUxZyUunMNey7QCDt9CKS6nhIeFEOSo2LuGxu57zbtcB3qUbokQ_zu_nfBUs9B4RU926XdM0Ho1xAULSUn_58AZGUBhyp7ECcKihd4gwxeLXoXfWHzqhDSZprowoQGfs_N64Chbz8L5pD5ne7p-jDSxZr6DQTqCPiKKUkpxUkheckq-e3zD3Cw5MUyunjnG41LLSrlqSUn44qCGdOLXwJsmuwCIZuwSwrbIPpeSc56qvgaAe0gNk0cHmxq3pPnC3dC5NpvY1bX_IiigLvto-xpL1L7xqQp6YMgPmM5nAoJPltZR2jGtpIMlpanbOSWAqrMkVEMIgAVM3fjNoK8D_8sOoauVFUSbGz-qesgdvnJt_qJqV0jAZAAy-pOgxPvP6w063y8AhypqbYsvJq61dWdItKQJBWtjJw8FDaY1ctilcD1Lu8j6ffFXDpBWwqTzfZjaspkW']
        elif service == 'AssetService.GetAssetVersion':
            return [b'jBFVrOjc7p7uFhNheHk7Ac9ArFHNJtLmwXn1Phx33AfLSLfB27Wl6XIwLUlJXn4AItEcvcY-JZO2M3dZHquhOybZpAuZlhioEkwfl8Hvpf0UXErIgEDb_H2gpZAFhf5LrYdgK1OdbyZeB_ZMs1YG0L72K2X92kRKlPwlykMrvqRc8w9plE3-WbOjw8AKaUI5dj-xS0QAmC7hUIMM_Q--AI9W45yYW7kL_rzuu-fob9JGrBdeQQLrH-vYVgnprHp4Q_zrP0O3kOS627XuyxN7zsLk9Hhn3wmRiUA5uRSVCR0=']
        elif service == 'BatchReqest_MakeCache_Login1' or \
             service == 'BatchReqest_MakeCache_Login2' or \
             service == 'LoungeService.GetLoungeChatList':
            ret = b''
            with open(service + '.response', 'rb') as f:
                ret = f.read()
            return [ret]
        elif service == 'LoginBonusService.ExecuteLoginBonus':
            return [b'fBBeL-V7mo1FiXqId0zt7gUHQrEkFFiiWqXkwU8UTy0Qg8Jld0b-eRd66AkqpdWG1QDqPxu0BegTbE02MpEMsiXMRbT4R2cvPeTh_GCejX_qYBwOBnzJgJochQhxpJOaDdCizProqShr6AVJwC1ZvamUoiy-lh3GcmcQvFe_S6_5QVlWlGvoSHtJps-Qm9bMrzXWu-ddh5zC-bXhPERxY3BNYFFaP7TfA_3bSOHWsK1dm1ebec0-JeMH8QQgvezYZx9eD2z6INOsjm2h3lk8S1YWc4Brtywaw1DFqsDHJXrl_eHoEtJj4fwdf5VeqR53q428JqXhmDVmU--3w_nb4dUhcrkfZ8_19gNZ05t4wVFeIrtgwW2LsTDitvihFp7rXzjRUX4WMDayqAWp6sA--CUOhUGTEbP3XkEHFqKYjr65OhFmFOx1zTkhUCKL1KDRKd7HcZkXw-IQ9QEMOaXKxg==']
        elif service == 'OfferService.GetOfferList':
            return [b'k3dqBgqcR2uhCrxCAoOUaBtAR8jMZ-cCYWgpNXAbX7X04pbYTUiZjRwHevdFuB9QVfUVbK_0cylXu8Mk_bP4eIWy53OONJuPe1tsWKtG1nZhK6lf3A8ypca2xwH3u_aB3WyuTThsGNXrFIdg6AGDtNF4kPdQ6Lqm0sqUfvyIT3DSpZXpjGuk1TJXVqAP4IJ0oG3Ei1an4Nieay0PPsge-Flp5CGZrxSQW6mkQP1A_Gtzikl5TikF4yk087kWre4K99Gf1GKI9Yi6vcm9eY6ypSynzK2Zk69KShYM7fTNhT1zEeKBzPuEr88GOqyROc_GKb48v0a3hR5ZW6rieShW79ECJWX9E3HXcHXr_gHttshhgYRFawzZmBV3WYMB5MtO8IhB8Q7gWjNcck8jDkfrFWSeVYgD2KxpCWaup-j2YjKPedB6xxypVvMm1H6Snn-rgcNtHZKmnor2WrsvGDI5vYQU1pFhigEF-cq0BJG8Od70ixtub6V4FS6v49BpNMhxI_i0EN_ZN1dBZs1SXhFV1pY_tgJm7nFW3wAM2ucxXu7mkrBJsVEjMk8veK2_NksJ7Dg4uB-r2xHtbDArPjgI8Y7HwGvmcUrH-yDf8PVgfF0IJJHF9ApQ65PKV5FxIhgJQPXNRo2Lzqw90oZFyPLPW8uGiZ4s8yqLZhRrRR3ZAEjDj3ATm3IlTIuEsqdroiTTTbCEZQXh7lw-CL_cXSbRQKkaT-Q8A5CK7vwUbzHvaceTsySPV4VG60wguh8bNoicJo3hcR0CajPS6jvGj6oWwCK1ud47jSw7y9PY5W8A0QSr6hgQIbIgWBY611TMmgv0DzrqQEVnllktZcvsfmSGQESuBTjSs0Odb5AkS-CSZbl32ppDNN8iraCDAqtwYlqDHtnsa_tWpmFgFWS1z5D2pN_ytiJc78RcvaM55yhMw4Cl4cVjbKezTaSFZa7l9Zq_LWQ-fp3M1C7V7yuW4nTPxCo4jDCFKUvZXpMk5Q7ejxZ9-BiSj_cnXbBLwKFvCG70DedemRsDo94IvdbMc0iDLxJ7YHefTyOUfV7QMqxuzTsVTEWoxA5Aa9JEQIamWyUv5eM1S15Vy9NnGObyeqFJe6daZ7pQhfqpV76Ld67yxsYl3oaNnjRxX-FB2YbZZXDrrwaOV1QCtCEchK9oEaywgrDz1p3EYxXiicZPeQjFRrgHIm5ZsF0lDRdmgIBsJpZ9qDx0A00czqj3ayBlg01-SlChuV5K03zzb79Y-8nK3qs9eFZdDesbKJ8p3QLaE6QKaPVQU9xkHL7J8EHMc9HKN_Ub-ivqzx4z6YN1ESZXkpeXNXm4EKcep5fc7GR3L7xKYD6GHpfcouk3n3LbYU9OdjW3XcwxWsWzS3yZT_u_CsPo1wmAxM_9bQZBjnGMLKpZrJpQ9NrevcCO56oaWpKWDhwqjletgLsIcidDM_6ImK8Q-soWHxW5vynDR82ooNvrrpe8wtlFnsbdh5pFQY3iwV8T3NmOiYCR-lg9Tz11S2-odYdXKngcdceqFZrIZJacGlOhr_--7jSD2lP4c06pTfqtNggyzUTMM1tRs4ki42bhBJyUHWk1yCyRXMNXpUn5PAxKLzAdL2Umz5Xc0VrNTcv1GQuCzbndnYy4SHLtmLFH4oSfeWXYttRStYwOag2OVkTHHcqfwBWb0jFMPgOBIu59pORxI8XIMbzMgqKlsB9UflWym6AeagZnBn4Ydt8FSBVm9CtzZMafbCa_8wofxLaAZO1wIXW4NLs1gUCwiAZUiTSJecS9bk4AatmENS5sZGl0ackZVyv5ENea4KcnNsTb209ATU1Vk_iGAapoYa5hmf7epVwnySjRhQx6CAkqYCT3TwJAfxfghBF8pVkZS1B6ZaTvBP4_dtYwzeM3gI-vSvRNsMHtGHbHRfNhEp60WU6_790hz7iie6HClyyVwiXBR7gT_9tKYwW4K4r84mNWYaRiEf1iiIj10fizgZfBmexuOAfJzMmvQqkvWvrl_5bjGsLk4bcr18hpr7tYJai6tC2RPM4MGT3yAS-wfHVXHQqmCsgzFJvmtFGKmvGQhYALsD5VxW66GbpqIDrpGghbZ7rmBA9zLltIYjuf30IVNe92HTw_1gU3aEbTqGPIvgFmQYCTQCxUa758yGo3DeWlfjpOsUggp7Z53i2HyVijvwWWQY_8kXmgjCVT9Ox91DRUdMBGNBPFI9C49bmG5ltjT5JD3sNhRKcnWFr_EoZWBgd6osdXbZiWowZH4QGrrI6lIRZxJxWpOX2iCnybGUlhu69wgiitHbocn8TzuEGWqfpIMZXg1-fhFRhjhPiTcgicC4rgb9bGPgHvajuTpXUUQEA-TI2KlPcsn1LR2BikEOHvXzOYKimr0QfnbhclPCGyKY_hTUuqz56RX6j1p3piVVVS1BHPQz7Nk9XbezYtxJ1HRjEYUMcpGBioWmLI8thzViwKnKXQRUHTmXMoWmbktkSBZJJulQPwgQGXssVph5ZZe3s4p9EMZp-2NfIhNy6YQWKvb_5UdTdh26swPV4_MqCHPn09k0fZF9sWEvD75pHHjuDxK8LiQIU_F84xO-FwzoNqqbEb4QZOkRzecg1HXli4X6q8fmD8X1EKOZkQ8ZHmT9nOybHcSkIegaInTYcee1cqDd3a9Sx_ubZVQqGnwektiDFIrypy3BzxZUqfXErug47jn1v8_OnhyMThO-tueh1U9GNiipZm_Ai7Q6JLAJ5LJjE76QnNUulLcONvQ1TUpRbal5ueg7CIFE8CQnibsukqxvSspqZNUxrrrO91XHA5EFoxXVzEA9vfuAzMK1O4XmK9IASuwUo0arQZDaB4d0IdS8aeePwpiQCiwjrE0E6JnJdz3WQ-Mj1V9Pl8swB8laAwuuw26aYpbeM-VuAU_keNybh30-GsCT7GtVkys_cdnBibkBQzGVBaWpSVfo9xKW5Fvd1JmWRC9FInF3Mted6lfNP9d6pWQLSooOKRPJbAUO29jMS8JUK8KMLyKe1IdGvHLdskq7D_XreTElx01z9wWE-ZBDe6PAM3ekynI-A9RgYCBMFHHDRhpYPH2VatJ8QvlXsU6bYh3-WxBFUSXeTPfLstmY1NbFDBQ7kACpc-OcJcfQv3rYNsfo7-56fiUAXd2594alEeAcUH8QaB1808NaWoiAWkg2MJoqCBcJ6g5on0CEiUklhVuLCg9MsoDtoPKfrVx1WQRtx579lArYqweNW1kY5loaAmHmDN9pLgg7TFIzNErEvCI0iTraQoy6P5jZjCbvGFXZH7Gp94IqqZpr78dZ9KxMCjDxgO8p5LKieoQMwuoqrKfj8CIpRABcjeezukxLx0Ke995zSDmRhVF8e5mdUOGe8Gng9BJ0_x5pGkr1z3wOjSwlmP04jCQYL_10FuQINu92HCHwq6jxNhJ_F0NSrl2zO-fv7LNrmqZUUKSJYeZ3PzeJzI9Oj6sSFONsWzrx1fIvOkMCkaSYkRSCka01v7ErEBl7y2Yq6SgN8QEHU6WZLHw_EDIUKwymO31LiIKmgMBX4uNUlWy9Z5pcK5zutMxEz7A1oTKy0YLSfT3jPFdnAFUaXjEp_rgJDYUwa1_ZzEvoWEXfVHOOR7OMIF2IW6-asYG1dcbdNh5ARBh9II2KL-vrcG7wZ3ynEhGWVWxXy9QgOyaH2OiL11oOA4i4sXgORe1Eg4NUwYBaDAgBdg_CkvxT6HlZ7Sutflbsl8zQh8dnFwX3snW4c0LZErI-QtHyfEhPRn9Byg48mSYzZd2dzDSn7qYoc-eB7v9vkbtFjWq3A_vtWKHZL0GvlbkPT95KFDRFz09Vd-YuEWY5NdwbKDU6BX3-NkDLcfTJHOKsoRQxJhF7GGKG5eeAyxM8HPGx_Tnl-zgvLGO3ogglrdMb0xAFSSdH9TWXipjCUUdul9mzDbuYnzyOhh74UoTcbob7ksFRMshRhnw19xH9fwUasFxAWK9Fsnr12VQWwZDFnhvs3-UVKEH6_GTbGhwPIf24sdiy7RSTTcFiQZ_AcDdEmiL-xDnrSPaUcOfQhl0ZTpeENc1uQGgopkb5Ydqr8UfT-UkSGGGW8nhXQrLxnImGeK8Vg6R0NJIPyW4KfUsp6exrdVnCBD2N95EUERJTwVr3nHOsOEM1S6NrCrbyR8By32kQa93KgU3DFvPTk3HTYpvHK1eqRYCdGVUTO3ui6oHt3_6H8ZCvSryKGcbyxcu3r3HrUE7sbAGxQpLpDpjU43CsvyVYq1ALddJD2nN34yMd509ogFBkYsyGKMpwioAH-4UpqUAhq-cgcvqgC1GfARH0dvO97rrL8_1jR-1CDUJ0Y95mAH7lgcmZ4noBXPcHraKD34PyomUG7HX_C1EN4237p4G7otpXtrKrtfR6MF-NjeMGae9EKyofu8bhZKZpbzvxSj-p-JrfYkGmUnRsEyGARGf5nnkpxp4IOYeiswX14CvvlyP2Up0ucG-h3SlEqTKQX_EUgPxvk4IgYIqUdbtXs3zk38HigUi51CB5C65dCvXa-ZZK0ICnOUjg3FB5Zlamv2ar5qLDLXGPySSzX4E2FoH3jcZ6-FYRd0aUa5Q74_2OHKixMNL40TYZpA1ETdczbTA9PQmq-C1qrxWAlgp6u2mXdkfaBsfEt5kZDeXmhhPb6iJmh9TriNSAzQMWVFDQeO63mj0xVnVSKMrnY4Fjdt8Vz8WpaEgY2xiGglWeJm7QyKvbjY9_oLzVFd5X1Am3tHV5E57uGL4R8jgPv_xU2U-y69UHGkmJ0cN-Nqqz5u_FYGdK6kmnl9Jyd3cjmjggmFQ2BFcpjkIoYWU33m4HeuVlwBZVk-y6hMOwgbAkdXf0hJYHGHYh-E7C9gpOIFwRwYGnb80cHcg3Vzo-fJ4H1-e5cvnpbFczESXhaQ8jg9aB6t8TQEp2CIhIxyNm9EBA-BZnPa-fX0H4K8Sma0XGCIGSXBKFRZ0W1ugFcYnjqpGiV9zfHggUuwKs-6G4k_UGkR-VJ0Jg-Q-gcVcVDmp7_lKvo6VKgjQFhV3S7i5wf2-OV5cGDUWlGCL-tAlG2WqYlChxBTZPdPyQ9fXqT_Kx2fkRpS-Wd7NhAzKmJEYC7Yserknac2RrfT3cuR-GIkg8xQXDrDB7QzNWp8tVZWPsecKe3PqnyYDNTGDUQ_GBd-1t1Ww_T0iGfdvB1V1wjdhpMr-8Z6GjoS1MUXvBS_gqHStUW1e3gtYpRR1GsrGojz3_-Oa7h4RJ4PNHYPfwCFHQJVYIyz1vbNcVXk8knTLbr2PvdU0vH3f3PP0hxvyIr25LqWGo-Pr1avYLxG89slUwGRpc_BEiGvBH_ZH3fPAI7YCcqPgbLcnoYCjkZdLbMbPJ4vTBADfsSEhXH2ENYOp4h4-6y8g0v_YwoHJSTOMgvYc8KqVAVqiTUpj45PX64XAwzyskLu--TQd8drTfpqlO2AL1c6i3PjHgbBahZG8agV__Kui2L_eVqTVo9Oivclr993oaHfBDxT44Sk0vwVrA5VsSHKIS8nFcAREgZiw6ry78p79xY9vgNZj_h3EysqryCBtjOkouo-YZudh-rY_6R-K6xr6kY91Hz_8IdwVi6jijrjiI6aDlZBiMN6oWbSoceRQz7UPeA_Cl0pcj-i0uKxEez0LStlhKawKGoINtcm2rK3d6eGmd-xrdxm9f8omZY-L5j1NOP_Z7VYHiCQTUkHWxICL0Eelg8v9MdhqDERtv9uzZNH2MfMf9K_nTaaEJMUdCkd-6xhszCJOBR8KXl0qQ2UpsG-SoIWNsOMpYe0vFQDElTJ0uez5lkyD4y0n8pNykhj03ubI5uDH7LvUYDWcOyPZs5WLgD2hiaqYX23BuzLVv4inm_fcwdcbbtP7SchlJYbUdNwqAL7xaoEnzDws5enhxnzYJEjFNlPE6NLVbKi3p3ZkOIRuokPvzZox0PqumG6LC8RgRHADPmYobGJTYDUz9a-e1cCZ2rdH5UXSngPcR1VMp7MjLLo0Ktp1QoK-seYXqOS0hwyJeVl92IRaS1_4NypQh4dXJxj48VItybCKA0Q_vbkiYI9m2wn_zJIEu_-9Y-qjEh9iPZjdubPz__b80VyUHyARHUBFwLzPEFTrIVTuD-N2YQCA9UucodJUj0xxyu76RmqIj02CPCsnvaGhP8n7XhRiOzS-zgj0HGEjKcURCTx5Wijaog4jfXIzLSDU2lgYgL7bHNe_vBvBeaKZzxw9h7F0ap8IQDe6Jvp1MEmkU86UOqj7yMHu908cUh9W9MlmsSJp7hxwy7e1OdXRUvw_-_5yNbfqc0WkuAeEf-HRO6Sfm8o0ZRh1QzN94ezTrWWfk8A5sSCGZm-']
        elif service == 'LoungeService.GetSelfLounge':
            return [b'HuEG4u7zUwTnL_I4jCBl30GPQWorKgxNl1oDkxdwmbk__gqvPY07nPKRNcz9nAEXmKEO_cOUGMKlxZBcrQmVXD6D-3m0AXtZnPkTe0zyo42ueQr75aFP4GRrYPtZwR7gviThTZB2VXggLdZnH3ZKtU9rrh4W1BwaNy3lsvvi4vL8CA9yeVI6Zp9rMcwFu_1DzKzcMWNNuDHQsyArN-JBEAU-dGTpyeYFiBUachBUfLVNnS7eYVNUxQ9tWZnmq7pCmp08QG8aT6BDq5jEeYdM_DVtIXWOXbByNvng_BCe5ancrFxIGciQbTTRNdALopNnW7SVNRhu0WcyOGdV2EC6Rxbu5ZlD8rBkOeEBGQRt74Q04AeHTlPFVcgsA3sB1GBWRMIYN8rkuE9GkEM8dmerTAzXK_E-mQex4dd1OriR95b5a4Dk65Nb_uYE2q87aAOuc15W3is_Iaq28Qh6DL6Uym_SYk7XZGv0v8Z38XwfWrjWhLn4GFQQSDkt-iWDkKq5kLpXMstGsLIcjsIhx5xhU6Uu6QfQzTFqu64qOxB04743L6IiL19S2Q_1KBHU1p7HEhsi-P7yKouaqZinepzAumBQp342k-phdGv7sp8_SIlbavJ6OCCD3g0eEYV0mqW1KQH8C8KFCboMu2BlgKppkZD741HJw7dyVR4HlmbSOy1ZLUumo47s7bNCevFia8NP1WxIJYrux82irwzNU7NJg4HlbU7ZCOSSz8yB5aMLxLpRvg5pDxK49XsysqV0h0Z5lzw-JTuWrhwjBcJxZ-LuAsMVKYSa60y9Tt43pUxQEcaKEVIzfDbCaO-Sg_pmiAPzqnUnfSuZ88_NZcbdmsZHcYBJSx0kkhbarb8wEJ1M2BEszuvrFg7Egb-3iikBDu4K3N-YCdT31AYg0mmguS9Z9hqadBHIe6d4pkzkErWaQnAg6E441twRl_yKKPNppexWYtE1zKHONME8j3qE_JyO6NOnJ7OhGow9nx8_FFZL18ocj_g0gBAD_YJhaNAQweb1DVxyGc2XDXJm467EAx6YVumQgkMcACD3XZN5byaYTZ9YDhdHrZYChvJOuc3Ntgy6XZDmDvFjt9qjYasmCtjaJ5_I4HuYsAMT4unamqbohImNdUzWA3_lBr-0YqPndMzwEoQZ6bsHrOh3Sun_F7lWH7AApZM23wn0jC7H5bX1Azqdh8moNJAlizwPU2XXbFLURQfK6fBZXmlx7QFd5o9Cay2YWPmJzdTKCpzhOTvcCFKkOJLMWXfDAcPEHeOEoy5224-_va5hT-NSqOFgL7BcvRGIu2Y_BRpK-7Hkbv1BWDXfmsk-rLTP07TFOIVJhxBgSHUgBwY7V7igxXOynsVbeJN6Utv29G5gFO-siibCyAiCVf3RSyhfUmj1j_dB68eSNrLFrj0WH1WFpa57Z4PzW8PINyuYP7KsiGF6LxKkL7JcbeUB9C77hYERSAtSXiwpdH4aG1qhw-3v_W74M-qtLFSpUq2irQ3oH8PsFRytVs8rtbx41LfYlGiBcZa6zOAkr5ZpqM_ddHOUz0y9Fmw1jhPReH8NXuyv4pfzbKlpg3-5x5S4NlTRcazuRfNFxboXT1SegSda160QHksVmBn8a8a_8hVXfy4hwOopRxnHehjU0na_h-urFKZE9lyGMmux7cyErhVKcqcnYA8AGuRPBkCDdFjlYiV2ijMqfydC42c9X637TqqXiqaEFfl5oGa3WGnWpeCpWDSotmM0Izb7PcjCmni8N5YtL07_IFJp942u-imTOIUOoA8vWhR2Ljc7YZ1TpcHKZzHLdU-KyG1Scz6_JMykbdXB2U75aSGhpH6ZPJRaY8t-XKlYcv9qHD9TNv0z28xz8W0raTNY2MLUzAb1SD7HkydHsCRoZerY_joJnmv1rwJ4Rec7Vfgx8PWwI5Nu8Z0cdif62-aqu8mChkKTaOJii4rViw1RDvACa80GPI4k9cVvbBEyZoba5hlhIOv-cIxZxVTKFKvtzxZGGoF4batzeFm5QfdMpsbmpHByKurRIDQ-YpcviZ-2y8cqEg6UmxaZOG-S9c8-uR7M1SkbsJJMg6SLXcF3w3QepSDOVuTJyAe3ESaRLpjSK_ZzfpBGhPGKwVmu-41fom_rARLn5ASdpEkt1RaKLWUARMZygeOr9eZavOPiS9RjV96360gHRY6WPA5_22_MjSex9OF4WJUkTOUI3yZM5Nwed2Xk8WyKPRtbtvpUOJGNT-0oVnCSUZPKroIR5CE13-UaI1_2dbht5mgER5KBUJAGmLL19Sfwpa0GmmSdlFaUc-cRcQniqM1ndNs1TphCQo0qWsR2rvdi83xMZXZpi-1CxokeLv1p4HLCOVS8Sd6zvUCcpU10HOm_inXaF6qTU2Q6Znb7IMQFZGpe2WV1ldLMS4bw6zxYr-lx2R4jmccoROMoG1lnB2G9sRjeTskWNqzwtBxEjvGr5W2O-ZFzDeaeioWnkzREs-f9JIzuSRNEBTDhIQ_8yWpE22V15yLVe4UGm1FwoV0jgGKl50nSQ0aZH5zC6iNZHeANgyjpHQJamg0zetCyP4Qj5dPXovX7KyyseaVCHX8EkocpA2ipTMZNDb4cXW_JldLcHg68bONZA5hfxIap64RJ62vp5i29-lho1EfduhF8wkiEEvqhrf6P6e8I8vT5aA04ZRs1jP3aMgR8mqqpERV-ojNovvDoP7jvJiCDci0fIXcbDoVAqyvuH__N9Jb_tqEP3Ol6ldgnyn5VJ5PdyR9vT4Wj5mdl3_UMhhWdTu56Ntwy34QpFeHhw3yD2Ze2XOJ83NfDjciMY0u7ymv_NB7cIT_I1s4PoolkOlYxx-yxmeHCEH2JuySBf0g2HtO1x_cYQMTpxEcHKXYDniGzgeJQd5Lb4FlU3a3IVXWdrbPm6PsInFV8Vj8mcTBZH-rK2rec6tThnzWpFS6OOsaXSnZTSupnzC5iqOIQCmFW32FoYwiSPOph61XB6GsAigJnbsdyJ4pUePuZSL_XULECFLbcAEVjk9kFXFFoclvPs1M3fc0O7yGSo2m3zyZ4N8UE2McInyylhq0WMToJsIoJNdRtM26nqLjyoZWisQe1jrEbtDKXkpzp0aom9wZx1Ym0LVWx-69F1DsVHjfZLr9GjzovNDt1HNzcrN_qcDhrweTm9oxmsQCnHd8EWVOLXZkJGkFKDnAHIzFINZvAltqg_-FTP5-hXSl-qte5081GBrhg9tZsvHu-bKGtv7BK93kx1x9nyplNF5IqplyEJnmn-7sFnUtzBas8M3dOz_naeuBFKDXr59SxrP8mPljJWx1bGFcw9JNMm6umMbARwAmqOOXXl1Ktsktn8u8o5Dfy9H89RzDZwvHXOJdz6nrzrYhSiEuO2NthAyFksD4-oXYB-k-QlQ585_vi1v1bS1olEFskSXNBNUt4cQ2Rp5AFvLJLnoOsXCPtRnfW8fDcspY7IEQuMezWNmDo5HMR4zovnfWAAmNbD7aoMKPkRgKji4ulZdS24kvGOatSVc_p6b1zyqbmolyQSUAKRkmOcAr8vXK4aQIpZWyxOMq1gs96bzolgjsguLlbWVNt3rAzIK29yzzYHZbstkaINWMYJWMp1steAzf9iYxeyV082UE9E_fgiI-RYnECoX4n4xEWHT_xfXzV6gl62pgl32hBTh8aN_dNZs2CR4D1MX1GWlUZQPAm6WRGoh5d1mViWkqEUon1kw1VglyyhE9fhVa17OWgSigQER1PSrNKRUKDAgT_YJCvcJzdOWqrrCf_UkOVZBwMpV18vj5TBx7uCpVrOjiXn2AfNaq-0LhtYAw1QLfeyb7VMmL1fRE5xlCy_y8ajh9aAvg0kp9QdyM23_wB-vWV9rRz0o3nVxhZIkxyAAFn79_8cnAMDv3s9UNhWeAbGkexaDNziH5jIJn15gMzD0_D-afV1hEGeMwLH2HB3S7qAQtPVfXWrMee0fWcr4L159YgF37XBxqEJv9hfaGXUVtcHrHVU9jzOEinJPUjjPVUdrsYodyrZJeFlBzQ1anxxo3f1t3kDnGlYMvU_RK2khQOn7W7D54qiRBi8jYK8Uo4soLQLu0QoOBFaga62vTUontxu93bHMg4GH2aKPZ6VosZrBMRZKw3LTYR-gsEGP1TfCqMGcoVn9ZOeMoiP1Ppgvl_YWGK7HzsDXKuE8RbEy_EuKOVkddVfkdPbNOYlJ0-5s-ihdW7C2tcdU7fHIHTQEclqT7wN2TXVpG7HzksDfmNtfHBf9m4yesJ4t6EmKnIrBFZ-ZEuhbJtwz1XoOvrAzd8-d27ayxnVzTyfZVikkZngCAKr99kZIokagWCIZapYlZ4hv1VRchM6eImMhp29bEdlWmZmLwWbQvn8BzVDKoQa8w4rNSQLWIH6WFMwQ_QbQ-zyrgNjrM2PDzUiiAgWcgsRWRbifb3NHXHiT1wytg_l7GrNQ01-LIOP3WWVg8dapVqkZWcE0OitLmyAJNogiC9fsGakKqg_zAG6n7gPUUVkqR3pEnMngbJNUQwRWlSKOucKHS3d73E8yo3uv3ggcXtXbMRg3uy9iDd5g9Tw0XJhEAxMqjIiJ0Shg1wpRyaBJ2rg1L0m8hr40Uy65GPi0_eoFQ28oTReYJjJVOOhf5AAu6OTrrZjAXB_7CSasYoHGMIANSF3B9v4onhNCR1Mx9CTW_pVoAzUxM-Ta3SOj5aZQmtCr3QjWpaSUVD763bc-tw-SsCaotQuji1ubglv7_nl4R5BZ6gY-u7ezDgoaWczkSaBsktaw6IZnEeLvs9X0d7cPO9AoBpVnxelLHMfpDKJ0084E5M0VCc_H42Tw4nW4bndC1tHzQi8GDM-RpmZxTUXeDhZs40-JGmYcLMTWUxSo5pDczjNvRqorl4U_Z_RPcijlDDD3Y6BFo3acfy4gU7lVmMZgJOJxyjuv69ThgRHOfTPiFG5PEVUV5BY7HlIC4mqRFwLJlDOt-xWWz8Gxf29N5Mm_tQnfc6KY5CUyiUNVUMVHUhJnOHS0B-QuFk8hkhminnqLaMGmn56sinmPg8sB1JpsVBzM7XRo5SMdxZon6KwgyHIOd1x_f1HJLGpQasv9y3nCcEkg0WWrxNRXnEhTp80Fqs1D6K8pdidVmkbhbksQeWpilMavpi_PWt7RGjLdo1Kr6mdUdOkwqYH2vMarQhCwODC4a_z8CLf_taqR0AgkhNLXhYF0W_aOQcmAw0PiFR5d6vCeTbV9Otvnm38J29iULQN75fKObTA1wYI-tPSUbJ6xAlhepIXvLsdmIYsrO_MfSa-VrFbsHEs51n40gCJyu8pfCXYOI1lVh63KhEvnFfPDrifHWM_IMzCZa8S73lM9Bm-CcQX_7x8qsSf_xmJbDJawzRnUFpLIt__M30WBIvTmo6KUgU52kKPq6xQTN43jfezkJ8gWefoJbg20nPMG2K_xCSFhz0kt_TxxFuuAx10Q8Id2PRR2FFQRwQNZkkhAoMgkzdtjh5-GXRIlmB9wACoAttrHkNdsEdlQyscR4zc_M9wUxRfzA7KYQ1QCK24qLUU6-Ik4ASfrxJvgOLFU1kFdCuWFnqBgn501F0SzBIIDqLSGWM1Q==']
        elif service == 'TheaterService.GetTheater':
            return [b'9YxtuiY2wJ4oLnVeVVau3P0ri5LaW97W325GejQrRwNYmPW40qOJxMcmPsRGqs7dG5d1YBwwIolY928w6tDj1umlb6MO0GWy2aiO2nPT1riqoa6nYJY9aNlnQ-V29geETEAxxWtbgVYf-oESiHLBs6_7XaGMUTzWCz81xOHO8IoLnmBlKpCsuV6KsWPqd1Hy4Vz07J0tQb6MY_QDehlJ776rBI5ibQNwVaSbR-aTvq_AIUDN782t-y6KFRUE4-1x74MujiG4RHxA22WRo406CaAFyt40hDV5MP2TFH_h9qUgyFw5BHXVc4wPqpqzTULT3nEbZ1CMhEM2jI4odbknmsPUZjfcDFovTS34oXaKH5EUVWrxljm39cDCk2Cn1gVJQrkDbegkp8bNO2FVcLB0KfIF5I0L5KinAhND1D9vuAgYOqDZO7oAIXVpgPmegJwXc6g8BrcOn0yt3sV41Bn3BDtzXv4YBqOjoetlYnA8kkrf2vcSluyGRy3Frd1r8LPuMpCnjzTrkvRAUc1-5Ko3S401t_xBHRB2nFQjzbRjittWqZnej7vDbwqDFAPXu_amfeeUMDtmhjUsi4wf-eJ9kFp6pbOaUVx4M3-uQgYtCDmZD7DJbE5BWHMAvKfp1M0F8va15uRXF3ENXcUil91ZrsESm6E1TF7gLrpDsezdTtE=']
        elif service == 'BatchReqest_TransTheater':
            return [b'_q64OfilU9_HkT6DXj2A1iI_t2_BedofsPuaWQMld-EImVuzi17EUDaGAmS_rjp9bnGnRYnKXoun3Ampchy32wwZwA33iViUxrHkz1lYLHlyzFyVpe3NwNPv3Bxt2XXq3Tj6rlVj6y8XlbrZ7TLt5ExrrOobjvOT9-aKxX0yydzDI0IUgmK4SmLY965zrXJa4mIdl3_SrPscKCRRoKUpKTmAZmxPjSeX2zjuxTcIUce2IAjjKSLE-kZr-lcLGZM4H57lkcq-mu5TuFRNl7ofRm1Bl53ra33GadSTTtklj9uHQM9VF0FPeH1N9Kl5ikrGZt22bIH5EA95LBemv1BKzKKDiVkMSISkcIICMI69nxOBgR18kqnlZHKeNTm_IGK5JwWHU1pA6UlXf7RAugUehRkD76tlqQ_ALndnb31vRjSU9rIQgzs67-fO7cZc-89kQa2JZHxneB9mlaqiCfBBEFj7QoyA5IC8_yRS_sSIMO1o6stYrqsTzc1r4y-TvHtGbm_6z6rMxoxTR1n3Jrn5LoR4Ek7naUSX3we9iv-i5zhnffeebBXtAZ5b-9utHSO_TmGvujEu4n5MoCCt94gbczncflEPUsJrlMaT1SDepG1b16pI8I-OQEoV1icS7L9lWmOS7LXmHCnIMxEZL0iOoMY_7zigvfxzS6OZpoj6SD7u2niim28qxxRjYpYQYB10B39Sjb1bI7UBdaRmA_m8cg-VMALm0Q_jSKL39sskK1QBPHc0A2AJs3z_JpVYdGZDR9EnyEgalY0jwpMT0SMuWmEx5aGVmFR8LMBzH0yioQ1yENGsWdoVr7wtf1u60ueJqhy62Mxy-WoQI3AV5hSOdW-LDEPZbGZpdhcIGOeL8ODqQKSJ8_27bZ8PX1_p-JIvZQKfBMpFJ_NPg2eYqxmOsmVs4hLZRWOpZQV57oLpKdueZQ5hbl3phsP-Ul5S8MDDn9StHv3ZILyrhftMFUgm-cSyJt8m17l3JjYs7oN4Vb8nzGAjoXE2-VQ63_x0sNgjI9MQXhW5lSQPdKQH3BM6mk8KOE0Z4wUCN0v28hWi3HGXt-IqTi953JuwYvr7Lo2A5zVSUvcmDe4xCIpOM-TCOiewnRyd94D0VzfS2Zq5D6ZS3CzFQiJ6Kr_3l8fIfLsFBV3zJplNg1ndZn8dDJtYeXDCTTBPSf2oXLyhB1dW0IVglEXWOUmBjNUB091Kz6ikZcp7yXNpF6bRIWE4sJutPw5ETVlolldqzks_cIM6sfPi7yYgFQ2W4Kho646FIjgYc1F-G48h0kl5U_cihqf9qtxxpbCbh7bS49DXIj9lNsdXo4v5os1aW-JAPbXD9-my2gst8VZBFvUdYyaSyoCwn6aIQbEU3ojP9Pny6jSyNQLn1b34Ahq_sIQVosHv5JeYOjYZm6G-Uh5AWn4Zo0rn4d4ui4ynp6ZJbcC-twioFbFMsFyfiRb5PZVG6VQQskrgtnTlwohCkcxJs9qX1HzTk2rOtUW56WdutTYS0E2vHsVaSC6dIRlvXPJsMx1NYlCPb4XAhkJIpH5Au0Z8uD0_Glm9_CpPJpwq_-7epNqd7_j_ex5RB6uSlu1Ckke-wubBQ8K8q3b4pslWDesZzlgbZRXQbXcfHGdy81wZ0DFKsAnBBprgjYH6duJM9KwHVB142UsaUqRRjrwQ0kaifWVR-OEBrwc7-U18ti0O1xQsARlUpSfCMLK32_E21w3AqW8RxEHZ-NVXNbjPr0A5a17iOQ-xy9LQ4yXih1cXoa67BYvo_khZXjhkF4Kj1KqdeP8rYBztzlQ1HwtbUWZTS4ScpwnNS9xrSTzsbpwaCCKbvE9pj4xciR8Jhsf7WEM0zd6bJBPDtcjLU2J4SLOoCFNUgxK9Ea-FQbQ-NNOBTZxw39bM_3Vftb0M0PM2nCS-hphl-Q0-xZMX8bVlQIWdznPvgh7Uaee6I2LxIud8amxvMolm7bzNEfk0_0U2EASszg2ksdkNJIPfN4lDtlittWo8Q_svUulRfB6CmbVhmxsAeCS8v1a_S1Mctza-e-p5Arc1G4VHgHZ2wMq6i1u5MRjruWafnADmInSbtrsLxbtZ7Od0KWjalG-YlL2qzaybPjr9lYaUf6OlxPtRcLCXSQpyA83ttLnttO2YVwzTbkO2T3d7dHBMJqijdDBosmO4Afa7ZJuGiq-Qlm-jLSqLlz-DQS0E9u6wiYLNhU1cPWFsBtBGr8KP9AYvoV-LFmRuyw-NHynZww6oD7KujbPdjUkb4SEqHI5klETLDtP-BrJRpyHb5QMMK94rl_Mpjix3imUpwhf-CG5U8g-evtUrTIpVp1Sb2cB3_iLhe3-w0DrqEf-MUQ5aY6Shb9nbc6gI7U_F3dv6M9nOY0AvJEx1Eif54rwmELYSb90d0GDDk7NTD0BGZEX6sl8Yb-LPI95PDA3meEYxoE6cba10DFaGNAMhZCX8pgQNCxAti6cfiXz7PlsQNiG16rEBnNvqybbvr7BT8d-ZeQTyENJug8PpQsYzLFxy1ldO_h73zyrcQdGGE6_7r4kc-6BWQr-ltbbwiF8EVRGF0-7AvgSZzh3i3EedJqb4MiIKl5sX6kRX7ZnpvbrEy-dpnXTpFyVBx5xHbQpajggan7FdGosjRELjXdqd0yzgO2JQqam_W1vMVBItvbQyPcWiDlcxG_gVMc03D7gEZyvYNL7xfrR_A1vBVMde5OYbvTOO-b1yjouhJgi06u3Q-jhQ2sMrWt0JBlBxHyLlDlGo74QIxa9MEqBHRrGz0o8MAMqMzOGb25Mup2dRSYh0srNV9ivHy9baTqGr4MQewJnLKvZe8qgR50W0kxoWRm2Q-rTkUkokTUZMAASTAU2DGCwY41U65lagNF1RNyA-VWihm2scYN08YnudzPodNv9TKp2hANfne5GQkBt4F6qHI-MevNvtz86Jv1Q5Zom9oorHQZZOWViKrZFORp4qcST1w535V_2o36oHsjdwKFACGiU7x7doO1KeaW8c9JJJ7_Qy4-URuaw8PF32yiV5AHetLev26UFGJa1HHBnzm4fNX6JdNzevU7JqB9j8IKABHqegL2nF0kjwqwSz6PCXELoK1DbEuNXrQcFjiXm5JNcjw5gD3KKgiLNyx-RAUjZ-_WKyU0IA5bJXQ83W7S7rGvaetmbyZ4eV4TDRca6nFvT_79ZJfgh3kI6r3BsofzZTy8YGlagol3klVIz29YDedAKOj84CcjSlGvQGK4eAQZSKR0mfG1Y5Rx4edFEJGxQOeKeBO7EIRDHV_Zu6FOn2BUogl3IfhW75b0SUFmwXXnIAeYIF47L5IZSiKrVIUXgvvjliJQNY9nQoDpsQ1oPywGPzQtuWmWoPhll5QCfahsQ6jhYNpqxv73VCivnB4BuSRtjCObAEGBpsWPvPZihC8vW7AJUm-LexS6Z3CHDXSru7vd6icg0nRWTlo4S0j4t52lLCl6YHMv7wga9vvutaQKFokXizUYQglC8u3MlIm9AgqOHtfj288x41oRr4CdXzJiFgqpvz7fF9vvXN9a45cfecfYLB6UxpbO02SfTpKguaJnsh2tOgxRwfdYoZdUHTxGg-fHvZzUOkm2itanIgqLJpwxmk3HCD6gn7Lod4sBdS6cekas2Lu4GDhhMkw9Bh9FYQFGPyH-OHnmxjH2cRKepLdEAwkYM6xvFHjdd4guMS1d47trd1PCoZ0MgLtTdOfH-mwnFFFk2qe_Mdt4mSY9TEVQ7BcOCL_KWEDD0HJ1FhH6XsudLXZCxIhejC7WMv1tUhd8mjxx_52l3ZSyqXVMldwTE3-yly_g3f9-0YUNt18lndz1jjw7l-yc0KqKKEXGicBpl26p7899w-ydt1rxD67fQ8-tOg2--Q_AAdC6tcMKRrXbXPk5rOq8zgbEUOS5LSqoDW2NRwElsFxGakXgsq5YZ7DMcFfpOCNrnVmcG5AYeq-zbzQCV7W3IpR9Yjc8VoNwDyajdCkA7gth8CDjk9SjdS-tG71tvLODncMIxhiihATtKKobyyjD7TBJM8selIniGjdPsuj5IbpenQkMy0LIOepFFxPCNveFD09lnY51fdxZ2bv36Js7YlNClQXEuULMxaXqnZ1xYGPSmKLJs4wNT-gS7r3MBJLCyYKjaHmEsf_sBxwNzUnIxK6oo3mJtECt3ejbTRlvd_tXoRQeyHP8WM-qpGD20HVXdv_1QahPj3igC_yiFDPWWZ0pm07psfgRav-oF4jvZjXPwmJGFm_m0EnXYYCD5daSTtFpm3FODeJ9bl__c7lR_OWJvCoszdtotxp65Dr4fDIYrAvjAwNLx6qkAOjCbhKV8bf09Bn2S_aevX3tUSRe6J2qXON3KzZSruvykX94_9atBtJaXO0ym1_CtVl90ErTnlo1sKF74rB2vghF8si5MQXqoImEEzBre6UwQQ_en9aujtJeVHUPly3CZLS_iFZ6MFJrIso_hH8m3jTcjuELtjDIhO2MuiXp_dq5Xx2v4emnQ5oOhO_fu_AoezukbhTc9AZ4kma9P8P4rcwBYztk06JvBKU4R4HLrfQP4PVzig_y9o7FRjjnhoDZ_M8Hc73-5p4686Kq46yVs2JEXIHBCd4JxGM5Mgnht7VrVcA1vF6KZ4ng==']
        elif service == 'BatchRequest_MakeCache_UpdateTheaterGameData':
            return [b'tSuyEm2RjsD4SQGG7lBf6f_aU5yxXVpc9DVTzLcEOtr-aW42lK7JZlKABnrXKFAqXBk2u7sPQaN2pMuwTl-tGwlw97Gy5tJ-BtcirDz-u3vsKAo4QxZSPdSDjU9oSL4qAcOV2GoKhq93jmRT0KiY_ucw1wSrHpg0jGC0wcnugC_OvDofz8tXYM8JqTVFfS9g0K9xbBmG8jgmgIRQ_2TWZyPWjwE6AeT9yP_9N5qkyaK693o5NFW2bmkq5IqqxYRrwY-CA7IUMmYOYrrz6T3cvIIYYri8nZ80U2DaAiialBafKne8LJsPiqhLQM0BQvpBqQDuplmsxz8l-b8-1JSWW683LctXXHPNOfxnZEmDyNkm3FF2xMX-s_dSaw_60uPOol3AONC2nTwZ1-2b1vExPhzygqxRhn4klhR4CM9LvNZbKZIdRAj19Cq55zK4-dP_RIcidnGYl0L09Mc2ISniFqdRUtMiOMCNYEQAbE6ZA-MFl8X7vIX2cyqOxO_m5T8YiF1YaJi-oV4-AHjp9MNRMW1ryNFhUSR85Dh9NDiD0-2McRPZLqQ28zsaPp1GMDAYWcEwOSeh2q3yqXVJjM_NZ-1aPNvvusgEEJ_wXpC_psIRmFwBETYbyypB9PUg1ZG5jCTQtTDC7aTR-QlYgGCiLJGvTDu1ksngLtqAKcsce4rF7MeYBKOaLWKRFLI7VsGkCZUZNGix-zfd_o_I8012F1yT_R9qdo-DNSKn3YpjklTrcuWwluxE60nS55AzMYQHApadUWQXQSbQH5PRhBhDzO6YMomf7WNwFQoX4oYDQfmvmsUAflOhtyZ357zFKkXRVb3nYy_WCNPf9w6tKpflEkWAqb9wEkHnhR6DY8fprktapCpg1NAwoJ-xxSFRtZ4vSg5Q739ouCocm3B65rfNE4dBxXE6Q5hMZOR4z1mW-vd5RP4oD3MBsKFl99jQWCBvetHSg_pOMy8xhbt4FIEyaGfkYjJmKXuGUQbBmARKOQwI8KT9Lhia-71qwjMbjxQ1alUgPCE5v0j5Z8g9KKpXRu4oB0vkkxiulfHNTG6eugONOeYOiZeN8j_5_DDq8sZz9STQ0hxa_64MeF5EzcIXVoetNqhLiz_RJxLinPCN3b9wdl8UwTMawiw6xKecVljuj0ed1ifIbpCoCSakteqYl2HyRzwZ6ipK3Tgx4pywmXV2CT3tW_6y_Y2RX16RX0gZmsgCb525o1zU6baqD-AaEv6qYY6AJ3qlp9rOgFaFgFv0iSTFLnJGAWftR7CYWcOA0bx14hPtQ4GZGftUd4-G7Twm2WF8KGP_sJ5W-4RCUcefMH7GR7FPpoOKHW9bs7hi3L6v_1u8su8vnu_APDceDNwc_7VXhoU0r_iIcw44_QgaFjAJajyuy1ufjM7bD9QyXR0MIbD3FE42IIHse5iv8ZciU8ZfDaygm-PIRqdP6YqwKwaOYIWOptBlGOURqKgY5HrwvCk3Eiors2yzpsPoej5-7QzNKqRmXSPz1kId2Kn_jdnU3hbVD0kLTnJ8Q76IE_82bGceXVccaa7pGkZU-LM5FTpu1miQdgyHT8ye0ovA1RbtiGHzBMhH1t7EHMZ88Z0tykYshp8DngvggwHN32MorvZH2yhQf6T5YwPrUV3t1y0UtKrpiPBufr3QPH8TjkyWHKadl-F6Z2ZffYSQFw4xqRoHMpa9bwsOLX9cNG56TdGHydwbMxmjd9Ks2qtRzYJjw3Z1URRQuIsKVgCh5JjoISxjOfylz6oLWaEVx7gpoTlRnYodX9AJIvnG3dR4YK6Z08La4UxkT3YSDTmjhp1dfyS1G_WzztgxY3pcluC06sE0_eYC7ZNcXsGaasuC7C0UVUF9vx7uE7UPkpOH2IX57cxMFsrkbKkE8_sHDyJihMKgWuGmL32h8k7EkMNZYx_3D1MrPdKXKjMZWuAsKf6HMNRNdw7lr3UOy_vr7zRAiWfkVkKjFBHxzxGPXExdp7HtMDPDKhZHf-o-VNcphQnCYbM0jRHNpjcQZWtEjc-M8sO_gvifze3mvLW7DalmMxEjxoV5UfTtWwOjjyACVluVs5JhCh_uh_QmSbQL36s3DQQtLe4y6gHzHSBG_JkzPFcwwtOoad1JFe9waP1cpTzlky5ifvJ-i0bsz6ckDoseOuwFrfx_OijA5NQ5ttZg_LQUFCoad5C4AsaQUeiQ3bATiX_lUPlNo_OcRXkzCS9QKk62ihzpkntX4_8nVtzpjBxupvcQceUgelzcuZoItMppIHjUZ8ovuDDkWDIU21Ed8PF_PlegqpCleRMTXk5PVBUAnksYmMVow8tfslS9n0N9Xx7sTAQquZ0ZQH-Otk5rhAeBOOrEWKJRhDJ5mjnKnKOkaELMra9D31VgODhbhQx-4zGh6-1EefJ9sc3oH9Mjxf_1dynbKQ15GIbBtU_LlnFTh3ct6zgjKuY3liBE69rUWoz24LDPnLmz-hqtbA5VNCF-Mu4cjEwwvzsQlmj9MQrxNQzGj5GoDMN3fnGuzHbTwqe6gcy32z81olnhPH4fx2Oj-q6GmCpGSkXGTGTqDkQh-FQbQNCctZ6h4hAYFOAS375uCvXmymc6qs98KucO4h3nskAdKMplAw6PPvpYtPJ9jKHoqwfWkDNlmDAKsGF__hMI9rEv9KPhffbyrM2AxKw4J3nu4kFlyYl7pSPT-aSFemDt36I1HpaT4OfIhyXHUWe1hmdE4VxrCXpVIYs2QXeYqUGMOxrBXEdK2e_wzWraI4PP1V1QidRwN9J8iaj9YaPsR0w5bELrEnAk7vDTV6Yhc8gk6vJnj_cqO16FwuIza9i5u0eXoZNuED59rQJrzeQJtIsaEmTnj7o7vsnmgYlgG1xfHxVppuHpBmxHll2HjKIjTeXAtCsx7POqd1Kg1Ao90VbyiUhlbQO0ov3odz8arPm2aL-EKaxqD8AnnHWpZXDvCAPi_kpdjgQnHHngyCIg2VH7TphqyNNvvb0IrT5bz--ZcZuBbVDUk4ZsL_zmIF5AofyJOt6T5tb_XMB68RsoXzdsuNbl6WWD4Vnj5jBui6Vwd7m_PbbfyMqv8Os57MclrLzB6PwHAgqFFWOfNinlYV-oVQzeyrtPX_5bYD3r-W9UvlhqvrXy5BufKcq3JFTE3ldh_N8EYd1nNXo6zLIrXKyUE3zU6oGDiqT7K-RNGEJ5CPRdpW0yvChj2Hg5xT1nH1qtwZg5QSmJP1ZHOJmSQfmNltJH12RJGYgj5de6KJap26rpmtflKxLa1HiSOAXCx7DY_5rSA2iP_uXR-uOzRt_vbWdXjHBgEabClL_9DmdQnNiSpL6uFEANftNyc4ezcRZ5mvuQ4RCUzeoud_C1lf0sYggMwRxPWnZSAo_0A2CZw0BvitVRCAq0quYO-BNq9tAQiY-Skhket8w4Q2DuxxX6Gy5bc1oiMcsLi5GJa5WRafreBkvHQ0eZXQ8LGkK7nHNNWmfHxSAAexzNVP6HBylGhm0gwyNmYMpEfN21kVi8MqYO4hSt1TUmXWtfZ5QzpkydTBUa8roR_1Z0rY617DD_9_ksNRJcelPqs9j2coyZ1_gTUJljUdFyUAaZwpRUUEDUbiASExWaDQ2Hprn07wvQOBM1idCScJbm_MG9ED6P6Tsh2944XOIffwPucjofdLzMAK9-BYtW0itojvjeO9dPvPI0ny4KJ2QE3wMmxNIIOoe8U0Xa-FRHukMksl0_xPUquReP-vnHEKmJyl5pWm1OJKXm5UAzu3in2I59g8pOpqVboHoyPHrL4GvVoeceKZY-FI5oJffUI0CKuPd3axKsj9X7hg9A0sffN0iCxzZkE4E6ZMoGgBG-crZ3ldV_Fd1R8OE0frR0A_d_uM5i8Wsmy_S_jAeqG8icqkyA0CJOT06lJ_B8ekitpmmao6_aiceFyJu_lD8gkD_FyeKGVb1ElBywY1Rt9VTlvhrGD4cfa7c6_4gEE4NiMIXBKvg7e7f3yaE0XSrpVjbSlLjDvO1LtYHydNKTs--uQqTBvME0uECoJlQuKmliEG4ctDHcvkzJEJJC50Mfj-h8MpKx8GujZmRdeOu1_QI7cfBegoQqTmqnQXUjoPyxnfF9ME_7uDCfWObkKhGC6rg1kXCHLTN-0FV2ROwV7PWNZFbfLOoUq3STQBTSqPqYzwTLsOd04hy0DKKFfC-8OS8IpUplVArYEQnJ5jfxXICTWF1KaGeP_ZcIH-8a7PwbaMudCSUxwu57FTfGzhvv6CJ-C6BSxAq21jHoBAWqiNAVgEMf_zvmNqVu1Dvi6i2YPkGr0U9vA_12JOrLOFiq5dsg3XVzUtQ0AntW9G23i_1hLoawxWLNCO6NYGlnDH0mWkOOu4jIWPgAxtmPV4O3I86XVjKSZ3O8JuBPfegjKDku5r3FBIjinTXGNGRQ7staeSDGX7retIPiCcI3T4oj0IfHHGHn4W9snnyOVpTV3c9bqhu6n71drLzotjh8hDSBnJw3BJ0QZH153NmUIrN_RvE0ID6wHv7pnTrXDgRnNmDup88T5Eh_WOnP43tDJjBCsv-1j_fFIn4-w9XJEwPQwc7gzjIJgtmqt-ggTXRSpQOuJUqt6I2KgnqtMowxWUK6z0oQmdZmuOjp2J2AQh6aQkF9Sf3B9Zm7oE_1EqilqloQyvq9bdQfL3oEQyOU3PpGcR_dsJxUcbr6xeQLkUDY4E7kwteiGt20fNVBYvcoObj1iTo7FNmZcXoI04l1nQpqfbPZaHxXqvQhF3Kz6_DwqdsHVx7wKjmJjIilUbZlUkT20hHeaUdX6ylFF5PL2w7EY5LyJTTCXPXEFDsHdR-3maHmcQ7EK5ugMfImjlCaXZeJ5sR1LxGu4RK0s3reHvQp1iu4lQXfVwsBpxUY51Tk19k1CCkk6-4NfkkP8CoOsD4C96cuJS7BNGaE3-CTIRqaVoVkFYijiPJOuTVvZV41WJ-dXkh4uuJntivFmgHWlnw-SAct9B348JZtzh6C-ttW_fgCMlSn-Vg0vPLnlFBMoTN0mWDkYEAh21KhNTMivOirsMYmwn22G0jklQrLhcZVq9A7pIjEJsmGYhMYTRM7uPoy0tQ8gfjXqPZVeUh9VGumK7DxTKi-HFM0PwidJzRwvu_pQaqMcikfM4isO714eab-wGoVZ0QPU39mMcC9RYPws3yun2CVYHy7qmR-Vp91iwYQDptJ0QCfphB3QNptfclyTIhif1GW7hZOh5TjiF5P17NV2X-bQ5j382WkKFxsHdqaRZ9GbhLRlDUnKF67l6-KnzPdlxRf3A0uch6wR2xtNW1QCnbJWFHLDHl3DDxaa_UOEMH-jGF6O_DRlB1ahbt0ji7Pi6DeoKHR-gt1FAczYuEs7PUFBq-2-EYk5FQYAmVs2OWEZ-PcJ06J_2JU01kQ2BW4ZmEgVMHLSjNMohT36-OuZHkHN9br3yrSt4wgjtpggH9hYTUwjrkATDvlOP5WQLtlip-bc07ReJuYnmlrz6ULxm_2cLSz-bUAqDiy7cpDqIb3sT6Ur412GciFGbkXLf7jSh6HTe7oHuWDSXf6SuL7idYIiEl1EZ8ywmNXIPJxNuH3_jt685NN5psqxDq8smBpxPG648c1Yp0vXV9A1KMQBHiK8UVAmsgp2PTZnc5t4a_ivaDsVg4jVVQAq8-V75zwyhJCyaf5WUlpM_IeypGhgl_Sl1GIGuk2sxzsJeM5Kg89xyljhhqWM6QiLm8rxjMmVyu84sMcZTywME9De6FyXTl1yXFH_GSPKpXlVHvnokjPc2NYFSLVq9nBCoSyskQXAoNmy-M9E-N3AiYpxJHCpt_WaXTnq8S06wdvUOHuHNGI5aIhkqURKC4XKYF8hIKGF6Vd51HN_rDT9DEr8Zccq6GD3auPwRUwq1wsAcF9icM3JtTkM0fMp2AqaZ_Fzg6MFX3xZbse86oyeGHquK2KIFB1DO86Ru0vLNg1PGD1Xx0EguItt9kfiBeDIn-a6oXvnS5RLrFse7_Y0qPyljLZ6UYid3uHMf3dWNCwwRb2Dx3aNa05_yfbIsAuWDSi465-aSUYH2aIA7vmdBZDRYe_2GEc1fVrCoWA2q-gMUBlXmC_PCDUa8ME6LiIY54mL_nVOG3gZQFsjENk-OKPXsHbnrplwJ47U9EzDXsMi5BPwmmq2l7HvhTnQlKIP9TWQ6e-R9itiopoWVZHw-SBCPemTbZ9aHNV9YBXv1gZjg_Q6yhalBWn6QhfSpsPuTnmujXZ6ahwLObG_yWf18UIGNzFFVR914Yh3Hugsl1oXu-4jdQHH_hDQnOiF4luhNOxi7xWzC4mWLc--xmQ1hBaiMsHnxnkUretguli0ekg3aXMauyOYN6Qmb-vjUNIdnqnzzGb3UNWv57f9rhATbX7o7eZW2z-_tOffAallpShzm860d2bqE7SWpJ1EgtYjLlICj6z1A6yhBZJ-e5U9K-I6vidFjHkxHQNSMP8DCTNH1y5LD4LGMsMH2siyTvMxP0g9Z23yj0XmuyXONYOV8lzj52Z-pj9oSW3ONIAcQ3kaKSYeuRPZwDHksOkp3M06i5fwq0-vl0GIGMvWvLrj6WEh5rIOnJMbfuUyd1RMK8JIxNtPdQaS_3xl3RpJiuQnjCqE2Oqlvq40gp7HorP_4b2qxhwutlOOSFKUQNkRRyxI_r3DSadHq5XqcBK4YTVs45DPUD0mC7UOGg01wyayA_eJJi-mqv9d8xeAV8XqiREU8mlUOOmi4_XNEJi1T4cNawI5KCX_tkyWmWV52VD3BT59tbYfCyjRMwsMv3KapsKRqbNYBZO66xJBUVX8GBrSz7c4n-x1lTRC8oV4CkBwsSEYNPhEJGgp0dFB7RNLh2gWvwCBSrlfUODKOLJjyT--grcvqXH--E48-6rdfkk1X8PZLu4wg5yEftKanAjPCTPO13RQUSWoA-Lq_87Up58Qy26NWB7d__-sLDFkIrnXZqvtZ0RjlmreaDGdTKllWkx']
        
    else:
        status = '503 Service Unavailable'
        headers = [('Content-Type', 'text/html')]
        start_response(status, headers)

        return [b'503 Service Unavailable']